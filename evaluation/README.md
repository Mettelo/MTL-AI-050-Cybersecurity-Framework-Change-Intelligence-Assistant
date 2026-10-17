# Evaluation protocol and results

## Domain benchmark
Create a stratified gold set of at least 40 alignment/change cases covering all six CSF 2.0 Functions, Govern, moved outcomes, wording revisions, many-to-many splits/merges and unmapped candidates. Two governance reviewers compare both durable documents and crosswalk before adjudicating final labels. Split 10 development, 10 validation and 20 held-out cases; keep entire connected crosswalk components in one split to prevent leakage. Score mapping pair precision/recall/F1, change-label macro F1, old/new citation correctness, inventory coverage, unsupported obligation rate and human impact usefulness (1–5). Unmapped candidates cannot be counted as confirmed additions/removals without adjudication.

Targets: Inventory coverage 108/108 CSF 1.1 and 106/106 CSF 2.0 outcomes; mapping pair F1 ≥0.90; adjudicated change-label macro F1 ≥0.85; citation validity 100%; both-version citations for matched changes 100%; unsupported legal/compliance obligations 0; human impact usefulness median ≥4/5; every exported register row reviewed.

Use precision=TP/(TP+FP), recall=TP/(TP+FN), F1=2PR/(P+R); report zero-denominator metrics as undefined, with counts. Macro F1 averages class F1; micro F1 pools counts. Citation validity=valid nonempty exact quotations / all quotations. Unsupported claim rate=reviewer-labelled unsupported factual claims / reviewed factual claims. Abstentions and nulls must be counted separately, never silently discarded.

## Supplied executable checks
`python -m unittest discover -s tests -v` exercises domain invariants and review/grounding controls. `python scripts/evaluate.py` reports frozen-demo structural checks to `evaluation/baseline_results.json`. This is a smoke/integrity evaluation, not a measured semantic AI benchmark. See the generated report for actual results and scope.

## Final experiment record
Save gold, split manifest, baseline predictions, local-model proposals, per-case adjudication and metric report. Record model digest, prompt hash/settings, hardware, latency and all invalid AI outputs. Include negative controls with missing facts, contradictory evidence, quoted prompt injection and unsupported conclusions. A valid citation is necessary but not sufficient for acceptance. Human evaluation and UAT remain pending until executed by reviewers.
