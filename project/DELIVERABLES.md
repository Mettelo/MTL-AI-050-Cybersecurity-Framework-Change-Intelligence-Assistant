# Deliverables — MTL-AI-050

| ID | Required output | Minimum evidence | Default location |
|---|---|---|---|
| D1 | Discovery & governance workflow | users; as-is/to-be migration review; 8+ requirements; scope; traceability | docs/01-discovery/ |
| D2 | Source & provenance pack | exact NIST files/URLs; versions; hashes; rights/terms; source inventory | docs/02-data-governance/ + data/SOURCE_REGISTER.md |
| D3 | Framework inventory pipeline | reproducible extraction; identifiers; text; Functions/Categories/Subcategories; validation | src/ + docs/03-data-model/ |
| D4 | Crosswalk graph | complete many-to-many relationship model; unmapped candidates; cardinality checks | docs/04-crosswalk/ + outputs/ |
| D5 | Deterministic change baseline | text/structure comparison; label rules; split/merge/move handling; baseline output | docs/05-change-baseline/ |
| D6 | Local AI impact layer | pinned model/runtime; prompt/schema; bounded evidence; raw outputs; fallback | prompts/ + docs/06-ai/ |
| D7 | Citation & obligation guard | old/new evidence validation; unsupported obligation/legal-claim tests | tests/ + docs/07-guardrails/ |
| D8 | Governance review product | evidence drill-down; accept/reject/edit; review notes; approval invalidation; register export | app/ + outputs/examples/ |
| D9 | Evaluation & assurance | ≥40 cases; connected-component split policy; gold labels; metrics; disagreements; error analysis | evaluation/ |
| D10 | UAT & technical handover | ≥10 domain tests; 3 user tasks; defects/retests; setup/run/restore/troubleshooting | docs/08-assurance-uat/ + docs/09-technical-handover/ |
| D11 | Executive change briefing & demo | 2-page decision brief; 8–12 slides; demo; retain/revise/pilot recommendation | deliverables/ |
| D12 | Final submission & contribution evidence | final SHA/tag; evidence index; CONTRIBUTIONS.md; individual artefacts/reviews | submission/ + CONTRIBUTIONS.md |

## Required demo cases

Show: one unchanged mapping; one material wording change; one split/merge relationship; one unmapped candidate; one unsupported impact statement rejected; one edit invalidating approval; one final reviewed register export.
