# Unthink S-arm evidence

SCCN: Semantic Context Compression: Next.

This is a bounded packet-to-prose reconstruction dataset: three historical
requests, three replies per request, seven model/surface configurations, 63
reply identities. It is not an encoder, a new language specification, or a
release of the current authoring stack. The original study and scoring were
conducted by Seam (Claude Code), 2026-10-22; publication synthesis by Sheila;
release review, extraction and offline verification by Arden; project direction
by James Mayo, Sheila Studios. AI-assisted scoring is not human assessment.

## Contents

- `requests/`: exact original S-arm user-message bytes, including the instruction.
- `packets/`: exact original scene packets, separately pinned.
- `sources/`: only the three scored line spans, extracted without rewriting.
  Chapter 5 slices cover lines 1-219 and 221-742; chapter 1 covers lines 1-56.
- `GRADER-ONLY-OVERLAY.sccn`: original fidelity overlay, not generation input.
- `PREPARED-CODEX-S.jsonl`: original prepared messages, including the neutral
  system line. PREPARED_NOT_SENT is historical preparation state, not a claim
  that outputs were never collected. The 18 saved Codex output receipts are in
  `outputs/`; their content corresponds to two configurations using these cases.
- `outputs/`: all 63 identities, with 61 byte-identical original files, one
  title-only redaction, and one marker replacing an unrelated private narrative.
  Codex JSON files retain their original recorded configuration and usage fields;
  other files are the captured text, not raw browser-provider wire transcripts.
- `IDENTITIES-S.json`: original mask IDs, configuration/request/sample mapping,
  original byte hashes, public hashes and redaction status.
- `RUBRIC.json`, `SCORES-S.jsonl`: original rubric and S-only historical judgments.
  Two free-text contamination comments are redacted; numeric scores are unchanged.
- `MECHANICAL-S.json`, `AGGREGATE-S.json`: S-only selections of saved measurements.
- `METHOD.json`, `BROWSER-CAPTURE-LOG-S.txt`: collection configuration, deviations,
  and S-only browser log with private work names removed. Source reports are
  attributed records, not newly verified provider identities or host isolation.
- `PROVENANCE.json`: original hashes, excerpt line boundaries and transformations.
- `qwen-metadata/`: nine unchanged S-arm collection receipts with request hashes,
  temperature, token limit, completion flags and recorded usage.
- `MANIFEST.json`: public member hashes and lengths. It does not include itself.
- `verify.py`: a standard-library-only offline verifier; it sends no requests.

## Verify

Run `python3 -B verify.py` in this directory. A mismatch or missing file exits
nonzero. The verifier checks the exact public file set, hashes, 63 identities,
complete configuration/request/sample cells, score arithmetic, saved aggregate
equality and text metrics for all 61 unchanged outputs. It is not semantic
rescoring, a new blind evaluation, or a repeat of model generation.

The original off-task output R2878 and title-redacted R1491 retain historical
measurements but are not mechanically rescored from altered text. Their modes,
numeric scores and denominator membership remain in every summary. An original
hash commits to omitted bytes; it does not let a reader inspect those bytes or
independently establish the historical content. Redaction is an explicit
reproducibility limit, not a replacement success or a silent exclusion.

58 replies have a prose-mode label, including compressed/expanded prose and
explanation-plus-prose. One was marked truncated. These are not 58 independently
certified complete or faithful scenes. 22 is the historical script's uppercase
swap-keyword flag count, not an exhaustive actor-error count.

## Repeating the reconstruction task

Supply the exact request text in a fresh context, retaining the disclosed
neutral Codex system line when matching that surface. Use three samples per
case and record the actual model, host, tier, date, parameters, failures and
outputs. Do not show source prose, rubric or overlay to the generation model.
Historical host versions, hidden prompts and sampling are not reproducible by
this release. No model-running client, credentials, internal provider wrapper,
or authoring system is included. Anyone repeating the task must arrange their
own authorized access. This instruction is not a promise that named models or
tiers remain available.

The comparison measures packet fidelity, not exhaustive source fidelity.
Nico's exit ordering differs between source and packet. The listening exchange
also distinguishes literal dialogue ownership from a summarized relational
promise. No length-matched prose-summary baseline was run. No controlled
binding ablation or general model-family ranking follows from these records.
The secondary P-arm prose claims are attributed historical context; P generation
inputs/outputs and unrelated-chapter baseline texts are outside this S release.

## Scope and permissions

James authorized this selected research release; Sheila owns publication.
This package adds no blanket open-source or commercial-use license and grants
no rights in third-party franchises, model services or the broader SCCN stack.
Source-fiction attribution and any necessary rights determinations remain with
the publisher; this technical evidence review is not a legal clearance.
Private narratives, personal histories, newer language drafts and internal
authoring tooling are excluded. Do not publish the parent `.private-review/`
directory or build script. Publish only reviewed release files.
