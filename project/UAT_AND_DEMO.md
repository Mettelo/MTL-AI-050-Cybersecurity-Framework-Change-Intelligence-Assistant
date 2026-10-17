# UAT and final demo

## User scenario
A governance reviewer traces a Govern outcome to mapped CSF 1.1 predecessors, inspects both texts, explains a split/merge, checks an unmapped candidate against both PDF documents, assigns an accountable owner in the review note, and exports the reviewed register.

## Execute and record
| Case | Expected result | Actual / evidence / reviewer |
|---|---|---|
| Fresh checkout and demo | Valid evidence-linked draft | To execute |
| Official source import | Stable IDs, expected counts and manifest | To execute |
| Domain review scenario above | Reviewer can correct/reject candidates | To execute |
| Missing evidence / invented quote | Validation blocks | To execute |
| Partial/pending approval | Export blocks | To execute |
| Modify approved draft | Hash mismatch blocks | To execute |
| Local AI absent or invalid output | Explicit failure; baseline remains runnable | To execute |
| Complete review | Only accepted rows export, citations and notes preserved | To execute |

## Final demonstration (8–10 minutes)
State the user problem and scope (1 min); show frozen resource provenance and ingestion (1 min); generate and inspect domain outputs (3 min); demonstrate an AI error or uncertainty and correction (1 min); show blocked and accepted export (1 min); present held-out metrics, reproducibility, limitations and next steps (1–3 min). Do not use a prerecorded successful output as evidence of an unexecuted live run.

## Sign-off record
Record date, commit, reviewer role, case result, evidence path, defects and final decision. Product acceptance remains pending until a real domain reviewer executes these cases.
