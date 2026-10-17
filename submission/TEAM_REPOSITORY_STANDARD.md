# MTL-AI-050 — Team repository standard

Create **MTL-AI-050-<team-name>** under the **Mettelo GitHub organisation** and add individual member accounts.

Record in the team README: master URL/reviewed commit, members/responsibilities, frozen NIST source hashes, environment/run instructions, final team SHA/tag and limitations.

## Required repository structure

```text
README.md
CONTRIBUTIONS.md
.gitignore
requirements.txt or equivalent lock
config/
src/
app/
tests/
prompts/
evaluation/
outputs/
data/
  SOURCE_REGISTER.md
  raw/
    README.md
  reference/
  metadata/
  curated/
docs/
  01-discovery/
  02-data-governance/
  03-data-model/
  04-data-quality/
  05-evidence/
  06-ai/
  07-decision-framework/
  08-assurance-uat/
  09-technical-handover/
deliverables/
submission/
  FINAL_SUBMISSION.md
```

Equivalent tool-specific folders require an explicit mapping.

## Data handling

Use the approved NIST CSF 1.1, CSF 2.0 and official 1.1→2.0 crosswalk files in the master data pack. The team may copy the approved raw files from master `data/raw/` or reacquire them from the official URLs, but must create its own manifest with requested/resolved URLs, filename, version, retrieval/copy date, bytes/hash, sheet/format information and reviewer.

The source files in the master are not a completed framework inventory, crosswalk model or change register. Those outputs belong in the team repository.

## README and contribution evidence

State:

> Create a traceable CSF 1.1→2.0 change register that preserves NIST mappings, distinguishes structural from substantive change and supports human governance review.

Simulated sponsor: **Cybersecurity Governance Lead**.

Preserve this limitation:

> A NIST crosswalk is not semantic equivalence and the assistant does not certify legal or framework compliance. Organisational-impact statements remain hypotheses until reviewed.

Every member links authored artefacts, at least one substantive peer review, and UAT/demo/handover contribution. Commit count alone is not Proof.

## Required project-specific artefacts

- **D5 Framework inventory/crosswalk ledger:** `data/curated/csf-change-ledger.csv` and `docs/05-evidence/crosswalk-and-change-contract.md`.
- **D6 Change-intelligence evaluation:** `docs/06-ai/change-evaluation.md` plus `evaluation/results.csv`.
- **D7 Governance impact policy:** `docs/07-decision-framework/impact-review-policy.md` plus `change-register.csv`.
- **D8 Framework-change review product:** `app/README.md` and `outputs/examples/`.
- **D11 CSF migration decision pack:** `deliverables/csf-migration-pack.pdf` plus editable slides.

Maintain D1–D12 / acceptance / test / UAT evidence with owner, reviewer, result/state and final-commit link.

Recommended team size: **3–5 people**.
