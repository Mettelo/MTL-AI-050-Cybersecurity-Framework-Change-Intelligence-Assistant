# MTL-AI-050 — Cybersecurity Framework Change Intelligence Assistant

## Business problem and user
Governance teams migrating from CSF 1.1 to CSF 2.0 need traceable explanations of changed outcomes and potential policy ownership implications. A textual diff alone confuses renumbering with substantive change.

**Primary users:** Cybersecurity governance lead, risk owner, control owner and policy reviewer.

## Working product
Align Core outcomes using NIST crosswalk relationships, detect changed/unchanged wording and unmapped addition/removal candidates, preserve split/merge cardinality, explain possible organisational impact and produce a reviewer-approved register. Full narrative sections are a documented manual extension, not silently claimed automated coverage.

**Workflow:** NIST CSF 1.1/2.0 Core exports + NIST crosswalk → versioned outcome inventory → many-to-many alignment → textual change classification → possible organisational impact → citations to both versions → reviewed change register.

This repository includes a runnable Python command-line application, source importers, a small frozen demonstration input, automated control tests, optional local AI explanations and a hash-bound review/export workflow. The baseline is deterministic; it is not represented as an evaluated language model. Meeting extraction and ATT&CK mappings are candidates. AI quality acceptance still requires the held-out evaluation specified below.

## Run locally at zero cost
Install Python 3.11 or newer. No paid APIs, accounts, cloud hosting or Python packages are required. Run commands from this repository root, with normal Python (never `python -O`). Windows users may use `py -3` in place of `python`.

```text
python -m unittest discover -s tests -v
python app.py run --input data/reference/demo.json --output runs/draft.json
python app.py review-template --draft runs/draft.json --output runs/decisions.json
```

Open `runs/draft.json` alongside its source. For every record in `runs/decisions.json`, change `pending` to `accept` or `reject`, and write a substantive `note`. Review all AI proposals attached to that record as well. To correct factual content, edit the draft, then review that final draft. Approval is a local attestation, not an identity-authenticated signature.

```text
python app.py approve --draft runs/draft.json --decisions runs/decisions.json --reviewer "Reviewer Name" --output runs/approval.json
python app.py export --draft runs/draft.json --approval runs/approval.json --output runs/reviewed.csv
```

Export blocks incomplete review, unknown citations, quote mismatches and edits after approval. CSV includes evidence, details, AI proposals and review notes. JSON remains the detailed evidence-linked minutes, handover or change register. Keep draft/approval together for audit.

## Use the complete official resources
Source: **NIST CSF 1.1 (2018), CSF 2.0 (2024), their Core exports and the 2024-02-20 NIST crosswalk**. See [data guidance](data/README.md) and [source register](data/SOURCE_REGISTER.md).

```text
python scripts/fetch_sources.py
python app.py prepare --source data/raw --output runs/framework.json
python app.py run --input runs/framework.json --output runs/full-draft.json
```

Raw downloads are local and ignored by Git. The bundled input is a frozen reproducible demonstration; it is not a held-out benchmark.

## Optional local AI
Install the open-source Ollama runtime and download a locally runnable model, for example the Apache-2.0 `qwen2.5:3b`. A 3B quantised model generally needs several GB of RAM/disk; CPU execution is slower. Record the exact model digest from your runtime, hardware and generation settings. Model/runtime downloads need internet once; inference stays at `127.0.0.1:11434` and requires no API key.

```text
ollama pull qwen2.5:3b
python app.py run --input data/reference/demo.json --output runs/ai-draft.json --model qwen2.5:3b
```

AI adds cited explanation proposals to existing records; it cannot approve, overwrite source evidence or execute operational actions. Missing/invalid citations reject the AI result. Quote validity does **not** prove semantic entailment: a reviewer must inspect every proposal. Large meetings/registers may exceed model context; select a documented bounded subset, record excluded items, or use the deterministic full run. No silent truncation is performed. If Ollama is absent or returns invalid JSON, use the baseline and report AI unavailable; do not claim AI evaluation passed.

## Evaluation and completion
Create a stratified gold set of at least 40 alignment/change cases covering all six CSF 2.0 Functions, Govern, moved outcomes, wording revisions, many-to-many splits/merges and unmapped candidates. Two governance reviewers compare both durable documents and crosswalk before adjudicating final labels. Split 10 development, 10 validation and 20 held-out cases; keep entire connected crosswalk components in one split to prevent leakage. Score mapping pair precision/recall/F1, change-label macro F1, old/new citation correctness, inventory coverage, unsupported obligation rate and human impact usefulness (1–5). Unmapped candidates cannot be counted as confirmed additions/removals without adjudication.

**Delivery gates:** Inventory coverage 108/108 CSF 1.1 and 106/106 CSF 2.0 outcomes; mapping pair F1 ≥0.90; adjudicated change-label macro F1 ≥0.85; citation validity 100%; both-version citations for matched changes 100%; unsupported legal/compliance obligations 0; human impact usefulness median ≥4/5; every exported register row reviewed.

See [project pack](project/README.md), [evaluation protocol](evaluation/README.md), [UAT](project/UAT_AND_DEMO.md) and [submission guide](submission/SUBMISSION_GUIDE.md). Automated integrity checks and a frozen demonstration are supplied; human acceptance, semantic gold and local-model evaluation are not fabricated.

## Scope boundary
A document/version change intelligence product, distinct from detection, vulnerability scoring, phishing, SOC analytics and compliance certification. It does not determine whether an organisation complies with a law or framework. Crosswalk relationships are not equivalence.

## Repository map
`app.py` review/export/AI orchestration; `engine.py` domain logic and ingestion; `scripts/` source acquisition and evaluation; `tests/` executable checks; `data/reference/` frozen small inputs; `data/metadata/` provenance and schemas; `project/` delivery contract; `evaluation/` metrics/results; `submission/` final evidence standards.
