"""Offline verification of released bytes, saved-score arithmetic and text metrics.

No API calls, new generations, semantic rescoring, remasking or file writes.
The two disclosed redactions keep their historical metrics, not recomputed text.
"""
import difflib
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent
SCENE = {'prose', 'compressed_prose', 'expanded_prose', 'explain_then_prose', 'prose_then_explain'}
FLAGS = {'binding_swap': r'SWAP|INVERTED|REVERSED', 'pov_violation': r'POV VIOLATION',
         'invented_withheld': r'invent', 'host_bleed': r'HOST-CONTEXT|host app|Thesias'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8-sig'))


def norm(text):
    for a, b in [('\u2019', "'"), ('\u2018', "'"), ('\u201c', '"'),
                 ('\u201d', '"'), ('\u2014', ' - '), ('\u2013', ' - ')]:
        text = text.replace(a, b)
    return re.findall(r"[a-z0-9']+", re.sub(r'[*_#>`]', ' ', text).lower())


def grams(words, n):
    return Counter(tuple(words[i:i+n]) for i in range(len(words)-n+1))


def metrics(text, source, packet):
    w, s = norm(text), norm(source)
    result = dict(words=len(w), src_words=len(s), len_ratio=round(len(w)/len(s), 3))
    for n in (1, 2, 4, 8):
        r, t = grams(w, n), grams(s, n)
        overlap = sum((r & t).values())
        result['r'+str(n)] = round(overlap/sum(t.values()), 4) if r and t else 0.0
        result['p'+str(n)] = round(overlap/sum(r.values()), 4) if r and t else 0.0
    result['longest_run_words'] = difflib.SequenceMatcher(None, w, s, autojunk=False).find_longest_match(0,len(w),0,len(s)).size
    for n in (3, 4):
        source_grams, reply_grams, packet_grams = grams(s,n), grams(w,n), set(grams(norm(packet),n))
        novel = Counter({g:c for g,c in source_grams.items() if g not in packet_grams})
        result['novel_r'+str(n)] = round(sum((reply_grams & novel).values())/max(1,sum(novel.values())),4)
    return result


def main():
    manifest = load('MANIFEST.json')
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and p.name != 'MANIFEST.json'}
    require(actual == set(manifest['files']), 'Missing or unexpected evidence files')
    for name, pin in manifest['files'].items():
        data = (ROOT/name).read_bytes()
        require(len(data) == pin['bytes'] and hashlib.sha256(data).hexdigest() == pin['sha256'], 'Pin mismatch: '+name)
    identities = load('IDENTITIES-S.json')
    raw_scores = [json.loads(l) for l in (ROOT/'SCORES-S.jsonl').read_text().splitlines() if l.strip()]
    scores = {r['id']:r for r in raw_scores}
    measured_rows = load('MECHANICAL-S.json')['rows']
    measured = {r['id']:r for r in measured_rows}
    rubric = load('RUBRIC.json')
    expected = load('AGGREGATE-S.json')
    require(len(identities)==len(raw_scores)==len(scores)==len(measured_rows)==len(measured)==63, '63 unique score/measurement rows required')
    require(set(scores)==set(measured)=={r['id'] for r in identities}, 'Identity sets differ')
    models = {r['model'] for r in identities}
    require(len(models)==7, 'Seven configurations required')
    require({(r['model'],r['req'],r['sample']) for r in identities} ==
            {(m,q,s) for m in models for q in rubric['spans'] for s in (1,2,3)}, 'Incomplete cells')
    sources = {q:'\n'.join(l for l in (ROOT/'sources'/f'{q}.md').read_text().splitlines() if not l.startswith('# ')) for q in rubric['spans']}
    packets = {q:(ROOT/'requests'/f'{q}_only.txt').read_text() for q in sources}
    checked, redacted, summaries = 0, [], {}
    for ident in identities:
        rid = ident['id']; score = scores[rid]; measure = measured[rid]
        require(score['req']==ident['req']==measure['req'], 'Request mismatch '+rid)
        require(all(measure[k]==ident[k] for k in ('arm','model','sample')), 'Measurement lineage mismatch '+rid)
        require(len(score['E'])==len(rubric['items'][ident['req']]['exact']) and all(v in (0,0.5,1) for v in score['E']), 'Invalid exact score '+rid)
        data = (ROOT/ident['public_path']).read_bytes()
        require(hashlib.sha256(data).hexdigest()==ident['public_file_sha256'], 'Output pin '+rid)
        if ident['content_status']=='unchanged':
            require(hashlib.sha256(data).hexdigest()==ident['original_file_sha256'], 'Original byte identity '+rid)
            content = json.loads(data)['content'] if ident['public_path'].endswith('.json') else data.decode('utf-8-sig')
            require(hashlib.sha256(content.encode()).hexdigest()==ident['original_content_utf8_sha256'], 'Content pin '+rid)
            recomputed = metrics(content, sources[ident['req']], packets[ident['req']])
            require(all(measure[k]==v for k,v in recomputed.items()), 'Mechanical mismatch '+rid)
            checked += 1
        else:
            redacted.append(rid)
    require(set(redacted)=={'R2878','R1491'}, 'Unexpected redaction set')
    for model in sorted(models):
        ids = [r['id'] for r in identities if r['model']==model]
        scene = [i for i in ids if scores[i]['mode'] in SCENE]
        fraction = lambda i:sum(scores[i]['E'])/len(scores[i]['E'])
        flags = Counter(f for i in ids for f,pat in FLAGS.items() if re.search(pat,' | '.join(scores[i]['drift'])))
        value = dict(n=len(ids),scene=len(scene),modes=dict(Counter(scores[i]['mode'] for i in ids)),
            E_all=round(mean(fraction(i) for i in ids),3), E_scene=round(mean(fraction(i) for i in scene),3),
            exact_full=sum(fraction(i)==1 for i in scene),
            N=round(mean(scores[i]['N'] for i in scene),2),P=round(mean(scores[i]['P'] for i in scene),2),
            flags=dict(flags),novel_r4=round(mean(measured[i]['novel_r4'] for i in scene),4),
            r8=round(mean(measured[i]['r8'] for i in scene),4),run_max=max(measured[i]['longest_run_words'] for i in scene))
        require(value==expected['S/'+model], 'Saved aggregate mismatch '+model)
        summaries[model]=value
    require(sum(v['scene'] for v in summaries.values())==58, 'Prose denominator')
    require(sum(v['flags'].get('binding_swap',0) for v in summaries.values())==22, 'Swap-flag count')
    print(json.dumps({'verification':'PASS', 'identity_count':63,'prose_modes':58,
        'unchanged_output_metrics_recomputed':checked,'redacted_output_metrics_not_recomputed':redacted,
        'semantic_scores':'Historical single-grader judgments, not rescored by this verifier',
        'summaries':summaries},indent=2))


if __name__=='__main__':
    main()
