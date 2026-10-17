# Submission guide

1. Fork/copy the project into the team repository; assign delivery, engineering, domain, evaluation and governance roles.
2. Reproduce the baseline from a clean checkout and official resources; capture commands, versions and hashes.
3. Prepare and independently adjudicate the gold set specified in `project/ACCEPTANCE_CRITERIA.md`. Lock splits before tuning.
4. Compare baseline and local-AI-assisted output. Publish per-case predictions, metric denominators, errors and rejected hallucinations; do not claim an unexecuted model run.
5. Execute all UAT cases with a domain user. Demonstrate citation inspection, correction, review rejection and hash-bound export.
6. Complete `FINAL_SUBMISSION_TEMPLATE.md`, include the 8–10 minute demo recording or reproducible live demo, and tag the submission commit.

## Required evidence bundle
Team repository URL/commit/tag; final report; source and split manifests; test logs; AI configuration/digest; gold/predictions and evaluation report; UAT signed results; privacy/licence notes; reviewed export with matching draft/approval; contributions and limitations. Use public/redacted artifacts only.

## Completion judgement
Inventory coverage 108/108 CSF 1.1 and 106/106 CSF 2.0 outcomes; mapping pair F1 ≥0.90; adjudicated change-label macro F1 ≥0.85; citation validity 100%; both-version citations for matched changes 100%; unsupported legal/compliance obligations 0; human impact usefulness median ≥4/5; every exported register row reviewed.

Report unmet gates explicitly with remediation. Citation checks, tests and a demo cannot replace semantic quality evidence.
