# MTL-AI-050 — Submission guide

## Release sequence

1. Finish D1–D12 and map requirements to deliverables, acceptance criteria, tests and evidence.
2. Confirm all NIST source hashes, inventory counts, crosswalk version and reviewer restore access.
3. Freeze inventory extraction rules, crosswalk graph, change-label policy, prompts, local model/runtime, gold cases and dependency lock.
4. Run deterministic alignment/change baseline and local-AI workflow. Preserve raw outputs, unmapped candidates, rejected obligation claims and failures.
5. Execute crosswalk/change/grounding tests and **three UAT tasks**. Resolve all critical/high defects and retain retests.
6. A distinct member performs a clean rerun from the frozen NIST files and reconciles inventories/mappings.
7. Produce a 2-page governance decision brief, 8–12 slides and a 5–10 minute demo for the **Cybersecurity Governance Lead**.
8. Complete `submission/FINAL_SUBMISSION.md`, contribution evidence and evidence index.
9. Tag the evaluated commit **`v1.0-mettelo-submission`** and verify reviewer access.

## Walkthrough

Demonstrate one unchanged relationship, one wording change, one split/merge, one unmapped candidate, one unsupported obligation rejected and one approved change-register export.

Explain why a crosswalk relationship is not proof of semantic equivalence or compliance.

## Required evidence bundle

Team repo/final SHA/tag; reviewed master commit; NIST source/hashes; inventory and crosswalk validation; traceability; baseline and AI outputs; held-out change metrics; rejected obligation claims; reviewed register examples; UAT/defects; clean rerun; handover; decision brief/demo; contribution evidence.

Reviewer records **ACCEPTED / REWORK / BLOCKED** with actual reviewer/date, simulated sponsor role and unresolved issues/owners.
