# SCCN Unthink: same scene, different sentences

## Semantic reconstruction from early compact narrative packets

**Sheila Studios · 31 October 2026**  
**SCCN: Semantic Context Compression: Next**  
[SCCN project and public evidence](https://github.com/sheilastudios/sccn) · [Field note](https://sheilastudios.com/field-notes/what-survives-when-sentences-do-not)

An exploratory research release. Original experiment and scoring: Seam (Claude Code), 22 October 2026. Publication synthesis: Sheila, with Arden's release review; project direction: James Mayo.

## Abstract

Can a compact narrative packet carry enough information for different language-model surfaces to reconstruct the same scene without a separate language manual? We report a small cross-configuration study using three existing SCCN Unthink packets, one ordinary translation instruction, and three responses per packet on seven model/surface configurations. Of 63 slice-only responses, 58 rendered scenes as prose. Among those prose renderings, average retention of the rubric's exact-tier items ranged from 0.65 to 0.96 across configurations. Reconstruction often preserved event order, relationships, viewpoint and withheld information, but did not recover the original wording: mean recall of source four-word sequences absent from the packet was only 1.8–3.3% across configurations. Actor swaps and other failures locate specific weaknesses in the representation and its interpretation. These are descriptive results for these packets and surfaces, not a universal compression advantage or a ranking of model families.

## 1. What was tested

SCCN is a compact textual representation intended to retain context that matters during later interpretation. In this study the task was **packet-to-prose reconstruction**, not training, a deterministic decompressor, or recovery of missing arbitrary sentences.

The material consisted of an opening scene from chapter 1 and two slices from chapter 5 of *Unthink*. These were existing, earlier-generation packets, not newly optimized for this release. James reports that the underlying slices had been used months earlier without revision. That historical account is distinct from the byte identities recorded for the tested requests. The retrospective original Grok example was effectively the same slice, with a small whitespace/content difference; it was not an additional scored replication.

Each primary request consisted of:

> Translate this into standard English as best you can.

followed by a blank line and the exact scene packet. The source prose and fidelity overlay were grader-only and were not supplied to the tested configurations. There was no separate policy, taxonomy, rule manual or file marker in this slice-only arm.

The packets encode events and relational constraints, not merely lists of nouns. Among the consequential distinctions are who offers to listen, who performs or receives an action, what a character does not know, and why a moment of warmth does not resolve the larger fear.

## 2. Design and changes during collection

The primary slice-only arm, S, contains three requests × three responses × seven configurations = **63 responses**. A fresh context was intended for each request. The Codex surfaces required a neutral system message, “You are a helpful assistant.” Browser-hosted services retain their own host instructions and defaults; that is an important qualification to “slice-only.” Qwen used temperature 0.3 and a 32,000-token maximum. Other surfaces did not expose uniformly controlled sampling settings.

The experiment initially included a policy/taxonomy/rule context arm, P. During collection, James clarified that his earlier demonstrations had used only the scene slices. S was then added and designated primary. P was retained as secondary evidence. **This is a disclosed mid-study design amendment, not a claim that the complete primary design was preregistered.**

Initial Codex requests without a system message were refused before dispatch. An early Qwen request exhausted a smaller token allowance without content; subsequent collection used the larger allowance. Those attempts are not quietly counted as successful S responses. The historical study preserves their records.

## 3. Scoring

The semantic rubric was constructed from the packets and source prose. It distinguishes exact-tier scene requirements from more interpretive observations. “Exact-tier” means fidelity to the specified item—not an exact-string match or a percentage of all possible meaning.

One grader scored masked responses. Scores were locked before opening the mask key, but the grader had encountered some response fragments during capture. This was **partially blinded single-grader scoring**, not an independent multi-rater evaluation. No inter-rater reliability estimate is available.

The headline retention statistic below is conditional on a response being classified in a prose-rendering mode: prose, compressed prose, expanded prose, explanation followed by prose, or prose followed by explanation. One of those responses was marked truncated by the grader. This is not a count of 58 complete, faithful reconstructions. Non-prose responses remain visible in the adjacent denominator. Each exact-tier item receives 0, 0.5 or 1; the statistic averages each reply's item fraction, with five items for two requests and six for slice 2. A conditional retention score is not an overall success rate.

Mechanical overlap measures separately compare source wording with response wording. Novel four-gram recall excludes source sequences already present in the packet, so literal quotations supplied in the prompt do not by themselves establish recovery of omitted wording.

## 4. Primary results

| Model/surface label at collection | Prose renderings / all replies | Mean exact-tier retention, prose only | Prose replies meeting every exact-tier item |
|---|---:|---:|---:|
| Perplexity free default, backend unlabeled | 9/9 | 0.96 | 6/9 |
| GPT-6 astra, Codex | 9/9 | 0.96 | 5/9 |
| Gemini 4 Argon | 9/9 | 0.86 | 3/9 |
| Grok Fast, free surface | 6/9 | 0.83 | 2/6 |
| Qwen 3.8 27B, hosted | 8/9 | 0.77 | 1/8 |
| GPT-6 luna, Codex | 9/9 | 0.69 | 0/9 |
| DreamGen Assistant, GLM 5.2 | 8/9 | 0.65 | 1/8 |

The final column conditions on prose renderings; expressed over every reply its numerators are unchanged and all denominators are nine. These are **seven configurations**, not seven independent model families. Model names are recorded collection labels, not independently audited provider/backend identities.

Overall, **58/63 replies rendered prose**. The other five comprised three Grok summaries, one Qwen packet translation and one unrelated DreamGen response. Scene rendering alone is not proof of fidelity.

The original report describes the successful reconstruction pattern as:

> Same scene, same beats, same anchors, different sentences.

This describes a pattern, not every reply or complete preservation of every scene beat. Across configurations, mean novel source four-gram recall among prose-mode replies was 1.8–3.3%. These are means, not bounds on individual replies. The metric lowercases and normalizes punctuation and compares consecutive word sequences; it is not byte-for-byte identity. Long matching word runs were short, and the packets already carried some quoted phrasing. The result is therefore **semantic reconstruction with substantial paraphrase**, not near-verbatim decompression.

## 5. What survived—and what broke

Strong responses retained ordered scene events, relational implications, viewpoint, withheld information and ending hooks. This is more specific than generating a plausible story from a theme.

But the failures matter:

- **Actor ownership:** 22 of the 63 S responses were flagged by the original aggregation script because their grader notes contained `SWAP`, `INVERTED` or `REVERSED`. This reproduces the saved flag count, not an exhaustive independent actor-error audit: other notes describe attribution errors without those keywords. Ambiguous subjects around pacing, wrist contact, stumbling and dialogue were frequent trouble spots.
- **Explicit bindings:** the later chapter-5 slice's explicit listening-offer and “not a mistake” bindings generally held. This is an observational design clue, not a controlled ablation proving explicitness caused the difference.
- **Figurative language:** a haunted-projector description could become an invented physical prop.
- **Opaque exchange labels:** a label for a consequential conversation did not always carry the conversation's intended meaning.
- **Withheld information:** some outputs supplied answers the packet required the scene to leave withheld.
- **Viewpoint and output mode:** some replies shifted to first person, translated notation rather than rendering a scene, summarized, or followed unrelated host context.

The DreamGen contamination is retained as a failed/off-task outcome. Its unrelated private narrative text is not part of this public release. An omission marker and provenance record preserve its place in the count rather than silently deleting the failure. A second, on-task response carried an unrelated private work's title; only that title line is redacted, and the response remains among the 58 prose renderings. Both retain their original recorded scores and pre-redaction output hashes.

### A source-to-packet error can survive faithful reconstruction

The packet places Nico's departure earlier than the original source does, while also retaining a later exit event. The rubric largely rewards fidelity to the packet, so a model can reproduce that order and score well. Similarly, the source has Mio ask whether Touma will listen and Touma promise that he will; the packet's explicit binding summarizes the offer under Touma. Preserving that relational promise is not necessarily preserving the original speaker sequence. **Source-to-packet fidelity and packet-to-prose fidelity are separate questions.** This study does not validate an automatic encoding process, nor show that the packets preserve every important source detail.

## 6. Secondary policy-context observations

The retained P arm adds a large policy/taxonomy/rule context. Its outcomes were mixed: astra's scene retention was similar; the four collected Gemini P responses scored strongly; luna often translated the policy rather than producing the requested scene; Qwen also exhibited packet-translation and exhaustion failures. Samples and denominators differ.

That secondary arm does not support a universal claim that more instruction helps—or that a manual never helps. The bounded S result is that many successful reconstructions occurred without that separate manual. The public release focuses on the S experiment; it does not expose later language drafts or the broader working stack.

## 7. Limits and reproducibility

This is a small exploratory case study: three related narrative packets, three samples per cell, unequal and partly opaque host conditions, one partially blinded grader, and no length-matched ordinary prose-summary baseline. There is no demonstrated semantic-fidelity-per-token advantage over such a baseline, no statistical family ranking, and no inference that the result generalizes to every genre or task.

Providing exact requests permits others to repeat the task. Provider updates, stochastic decoding and host behavior mean repeat outputs need not match the saved text. The evidence release supports inspection of this sample; it is not a guarantee of current hosted-model availability or behavior.

The package distinguishes unchanged original artifacts from publication-derived tables, scripts and redactions. Its offline verifier checks byte identities, recomputes the S-arm score aggregates from the historical judgments, and recomputes text-overlap metrics for 61 unchanged outputs. The two redacted outputs retain historical measurements; their original text metrics cannot both be reproduced from the public files alone. It does not independently regrade semantics or reproduce the secondary P arm. No new model experiments were performed to prepare this release. Public source material is restricted to the study's three scored source spans and grader overlay, not a release of the broader manuscript or private agent history.

## 8. Where this led

These early SCCN packets became a starting point for a broader investigation: not only how compact representations preserve narrative meaning, but how they can carry relationships, constraints and frameworks for judgment. Subsequent work has explored those directions in agent behavior and authoring tools. This study reports the reconstruction evidence; those later developments warrant their own reports.

**The question began with what a model could reconstruct. It grew into what a compact representation could help it do.**

---

Prepared by Sheila Studios. James Mayo directs the research program; Seam conducted and documented this experiment; Sheila prepared this publication synthesis with Arden's release review. AI-assisted research and scoring are disclosed, not presented as independent human assessment. Any third-party fictional setting or character rights remain with their respective holders; no ownership of those rights, affiliation or endorsement is claimed. Public release does not add a blanket open-source or commercial-use license to the broader SCCN stack. Contact: https://sheilastudios.com/contact
