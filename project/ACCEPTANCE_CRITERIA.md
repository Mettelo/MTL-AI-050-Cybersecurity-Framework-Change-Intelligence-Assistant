# Acceptance Criteria — MTL-AI-050

| ID | Acceptance gate | Objective pass evidence |
|---|---|---|
| AC1 | Scope and requirements | ≥8 prioritised requirements mapped to D/AC/tests; approved migration-review workflow |
| AC2 | Source reproducibility | NIST versions/URLs/hashes frozen; source inventory complete; no hidden live dependency |
| AC3 | Inventory completeness | 108/108 CSF 1.1 outcomes and 106/106 CSF 2.0 outcomes represented or discrepancy formally evidenced |
| AC4 | Crosswalk integrity | NIST many-to-many mappings preserved; split/merge cardinality tests pass; unmapped candidates remain explicit |
| AC5 | Baseline change logic | deterministic change labels reproducible with documented rules and stable evidence IDs |
| AC6 | Mapping quality | mapping-pair F1 ≥0.90 on adjudicated held-out cases |
| AC7 | Change-label quality | macro F1 ≥0.85 on adjudicated held-out labels |
| AC8 | Local AI execution | actual local model run with pinned model/runtime/settings; raw outputs preserved; no paid dependency |
| AC9 | Grounding & citation | citation validity 100%; matched changes cite both framework versions 100% |
| AC10 | Obligation safety | unsupported accepted legal/compliance obligations = 0; impact remains explicitly provisional |
| AC11 | Review control | every exported row has reviewer decision/note; material edits invalidate approval; pending review blocks export |
| AC12 | Evaluation integrity | ≥40 cases; 10 dev / 10 validation / 20 held-out; connected crosswalk components do not leak across splits |
| AC13 | UAT & defects | ≥10 domain tests + 3 user tasks; zero unresolved critical/high defects; repairs retested |
| AC14 | Reproducibility & cost | different member completes clean rerun; no paid GRC/legal/AI service required |
| AC15 | Submission integrity | evaluated tag/SHA fixed; reviewer access, limitations, evidence index and contribution records complete |

Human impact usefulness target: median ≥4/5 with sample size and reviewer disagreements reported.

Final release state: **ACCEPTED, REWORK or BLOCKED**.
