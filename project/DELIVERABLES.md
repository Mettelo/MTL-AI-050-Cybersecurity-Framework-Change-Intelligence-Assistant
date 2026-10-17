# Required deliverables

| Deliverable | Evidence required | Accountable role |
|---|---|---|
| Local application | CLI run, validated JSON draft, reviewed CSV | Software engineer |
| Ingestion and frozen resources | Source URLs, release/date, SHA-256, row counts, parser logs | Data engineer |
| Domain candidate generation | Evidence-linked records and documented failure modes | Domain analyst |
| Local AI comparison | Exact model digest/settings, prompts, baseline comparison, invalid-output log | AI engineer |
| Evaluation | Adjudicated gold, locked split manifest, per-case predictions, metrics and errors | QA/evaluation lead |
| Governance | Risk log, privacy/licence notes, review audit and rejection cases | Governance reviewer |
| User acceptance | Executed UAT, user comments, defect resolution and sign-off | Product/domain owner |
| Final submission | Team repository, tagged commit, report, demo and limitations | Delivery lead |

Roles may be combined in a small team, but an independent second reviewer must examine semantic gold and final claims. No person may count their own unreviewed AI output as accepted ground truth.

Domain output: Align Core outcomes using NIST crosswalk relationships, detect changed/unchanged wording and unmapped addition/removal candidates, preserve split/merge cardinality, explain possible organisational impact and produce a reviewer-approved register. Full narrative sections are a documented manual extension, not silently claimed automated coverage.
