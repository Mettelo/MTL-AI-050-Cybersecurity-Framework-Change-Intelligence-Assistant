# Data Guidance — MTL-AI-050

## Approved core resources

### S1 — NIST CSF 1.1 Core

Exact URL:

https://www.nist.gov/document/2018-04-16frameworkv11core1xlsx

### S2 — NIST CSF 2.0 reference/core export

Exact URL:

https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all

The endpoint currently returns a downloadable framework export. Teams must record the actual resolved URL, content type, filename, byte size and SHA-256 rather than assuming the extension or format.

### S3 — NIST CSF 1.1 to 2.0 crosswalk (2024-02-20)

Exact URL:

https://csrc.nist.gov/csrc/media/Projects/olir/documents/submissions/CSFv1.1_to_CSFv2.0_CROSSWALK_20240220.xlsx

## Raw-data strategy

Freeze all three source files before development. Record:

- requested and resolved URLs;
- retrieval UTC;
- filenames;
- bytes;
- SHA-256;
- workbook sheets/structure;
- NIST publication/version metadata;
- parser version;
- inventory counts.

Do not overwrite frozen source files.

## Required inventories

Build explicit outcome inventories for CSF 1.1 and CSF 2.0.

Minimum fields:

- framework version;
- Function;
- Category;
- Subcategory/outcome identifier;
- exact source text;
- evidence/source reference.

Do not silently infer missing mappings from model memory.

## Crosswalk model

Represent the NIST crosswalk as a relationship table/graph so one-to-many and many-to-one mappings are preserved. A crosswalk edge is evidence of a relationship, not proof that the two outcomes are semantically identical.

## Evaluation cohort

Create at least 40 reviewed cases across all CSF 2.0 Functions, including:

- unchanged/similar wording;
- moved outcomes;
- wording changes;
- split relationships;
- merged relationships;
- Govern-related changes;
- unmapped candidates.

Keep entire connected crosswalk components within the same dev/validation/test split to prevent leakage.

## Local model

Any local model used for impact explanation must be separately recorded with origin, licence, digest/quantisation and runtime settings. Model weights are not committed to Git.

## Durability

The frozen NIST files and hashes form the assessment baseline. If a live export changes, do not silently refresh the cohort; create a new source version and rerun affected evidence.
