# Submission Guide — MTL-AI-050

## Final release sequence

1. Complete D1–D12 and reconcile requirements → deliverables → acceptance criteria → tests → evidence.
2. Freeze all NIST files, inventories, crosswalk graph, gold labels, model/runtime, prompts and dependency versions.
3. Execute deterministic alignment/change baseline and local-AI held-out evaluation; retain raw outputs and failures.
4. Run guardrail tests, ≥10 domain tests and 3 UAT tasks; retain defects, repairs and retests.
5. Demonstrate unchanged, changed, split/merge and unmapped cases; reject one unsupported obligation claim; show edit/approval invalidation.
6. Have a different member perform a clean rerun from documented resources.
7. Produce the governance decision brief and demo.
8. Complete FINAL_SUBMISSION.md, CONTRIBUTIONS.md and evidence index.
9. Tag the evaluated commit `v1.0-mettelo-submission` and verify reviewer access.

## Required evidence bundle

- final repository/SHA/tag;
- requirements and traceability matrix;
- source/hashes and inventory reports;
- crosswalk graph and validation tests;
- gold labels/split manifest;
- baseline and AI predictions;
- metric report and raw failures;
- citation/obligation-guard results;
- reviewed change-register examples;
- UAT, defects and retests;
- independent rerun record;
- zero-cost declaration;
- technical handover;
- individual contribution evidence.

## Completion rule

A textual diff, screenshots or fluent model prose are not sufficient. Reviewers must be able to reproduce the inventories, mapping relationships, change labels, AI impact hypotheses, citation checks and human-reviewed register from the frozen sources.

Unmet gates remain REWORK/BLOCKED.
