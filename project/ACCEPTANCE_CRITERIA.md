# Acceptance criteria

## Functional gates
1. Fresh checkout runs the bundled example with Python 3.11+ and no paid dependency.
2. Official-source preparation succeeds and records provenance; source identifiers survive into output citations.
3. Every candidate has at least one resolvable exact quotation. Missing data stays explicit.
4. Each record receives accept/reject and a reviewer note. Pending or partial review blocks export.
5. Editing any part of the draft after approval invalidates export.
6. Repeated baseline runs on identical input yield the same content hash.

## Semantic and AI quality gates
Inventory coverage 108/108 CSF 1.1 and 106/106 CSF 2.0 outcomes; mapping pair F1 ≥0.90; adjudicated change-label macro F1 ≥0.85; citation validity 100%; both-version citations for matched changes 100%; unsupported legal/compliance obligations 0; human impact usefulness median ≥4/5; every exported register row reviewed.

## Measurement protocol
Create a stratified gold set of at least 40 alignment/change cases covering all six CSF 2.0 Functions, Govern, moved outcomes, wording revisions, many-to-many splits/merges and unmapped candidates. Two governance reviewers compare both durable documents and crosswalk before adjudicating final labels. Split 10 development, 10 validation and 20 held-out cases; keep entire connected crosswalk components in one split to prevent leakage. Score mapping pair precision/recall/F1, change-label macro F1, old/new citation correctness, inventory coverage, unsupported obligation rate and human impact usefulness (1–5). Unmapped candidates cannot be counted as confirmed additions/removals without adjudication.

## Evidence for sign-off
Attach test output, source/split hashes, raw predictions, metric report with denominators, independently reviewed failures, model/no-model comparison, UAT results and known limitations. A 100% citation match is only structural grounding, never proof that the claim follows from that quote. Evaluate factual entailment separately by domain review.
