# MTL-AI-050 — Cybersecurity Framework Change Intelligence Assistant

**Mettelo Project Studio**  
**Track:** AI Engineering / Cybersecurity Governance  
**Engagement:** Simulated framework-change intelligence product  
**Team:** 3–5 people  
**Delivery window:** 8 weeks  
**Core completion cost:** £0 incremental software/service spend using existing equipment

## Business problem

Security governance teams migrating from NIST CSF 1.1 to CSF 2.0 need more than a textual diff. Renumbering, split/merge relationships, moved outcomes and wording changes can be mistaken for substantive control changes. Manual comparison is slow and difficult to audit.

The organisation needs a local assistant that aligns framework outcomes, distinguishes mapping from substantive change, produces evidence-linked change explanations and lets human reviewers decide what may require policy, ownership or control review.

## Commissioned decision

> Can a local AI-assisted workflow create a reliable, traceable CSF 1.1 → 2.0 change register that reduces manual comparison effort without inventing legal obligations or claiming compliance?

## What the team will build

Build a working local product that:

1. downloads and freezes CSF 1.1, CSF 2.0 and the NIST crosswalk;
2. creates complete outcome inventories for both framework versions;
3. preserves NIST many-to-many crosswalk relationships;
4. detects unchanged, wording-changed, moved, split/merged and unmapped candidate relationships;
5. distinguishes crosswalk evidence from team-derived change labels;
6. runs a local open-weight model to draft bounded impact hypotheses;
7. cites both old and new framework evidence for matched changes;
8. blocks unsupported legal/compliance obligations;
9. lets governance reviewers accept, reject or edit every register row;
10. invalidates approval after material edits;
11. exports a reviewed change register and decision brief;
12. evaluates alignment, change labelling, citation accuracy and impact usefulness on a held-out gold set.

The product does **not** certify compliance, perform legal interpretation, automate policy changes or claim that a crosswalk means semantic equivalence.

## Practical use case

A cybersecurity governance lead selects the frozen CSF 1.1 → 2.0 migration set. The assistant shows aligned outcomes, flags wording or structural changes, proposes possible ownership/policy implications and provides citations to both versions. Reviewers validate each row, reject unsupported implications and approve a final change register for internal planning.

## Approved resources

- NIST CSF 1.1 Core
- NIST CSF 2.0 Core
- NIST CSF 1.1 → 2.0 crosswalk

See [Data Guidance](data/README.md) for exact source URLs and preservation rules.

## Required workflow

```text
Frozen CSF 1.1 + CSF 2.0 + crosswalk
        ↓
Outcome inventory
        ↓
Many-to-many alignment graph
        ↓
Deterministic text / structure comparison
        ↓
Change classification
        ↓
Local AI impact hypothesis
        ↓
Citation / obligation guard
        ↓
Human governance review
        ↓
Approved change register
```

## Minimum evaluation standard

Create at least 40 adjudicated alignment/change cases spanning all CSF 2.0 Functions, including Govern, moved outcomes, wording changes, many-to-many split/merge cases and unmapped candidates.

Release targets:

- inventory coverage: 108/108 CSF 1.1 outcomes;
- inventory coverage: 106/106 CSF 2.0 outcomes;
- mapping-pair F1 ≥ 0.90;
- change-label macro F1 ≥ 0.85;
- citation validity = 100%;
- both-version citations for matched changes = 100%;
- unsupported legal/compliance obligations = 0;
- human impact usefulness median ≥ 4/5;
- every exported register row human-reviewed.

## Zero-cost implementation

Use Python, local files/SQLite, pandas/openpyxl as needed, Streamlit or CLI, pytest/unittest and a local open-weight model via Ollama or llama.cpp. No paid API, legal database, commercial GRC platform, cloud inference or hosted vector service is required.

## Delivery standard

Final acceptance requires reproducible source acquisition, complete inventories, crosswalk-preserving alignment, deterministic comparison, local model execution, evidence-linked impact hypotheses, obligation guards, human review, measured evaluation, UAT, independent rerun, technical handover and individual contribution evidence.

See [Deliverables](project/DELIVERABLES.md), [Acceptance Criteria](project/ACCEPTANCE_CRITERIA.md), [Data Guidance](data/README.md) and [Submission Guide](submission/SUBMISSION_GUIDE.md).

## Scope boundaries

This is framework-change intelligence, not compliance certification or legal advice. A NIST mapping/crosswalk relationship does not establish one-to-one semantic equivalence or prove that an organisation satisfies either outcome.

---
**Mettelo — Built for What’s Next**
