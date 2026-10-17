# Project brief

## Objective
Deliver Cybersecurity Framework Change Intelligence Assistant for cybersecurity governance lead, risk owner, control owner and policy reviewer.

## Required use case
Governance teams migrating from CSF 1.1 to CSF 2.0 need traceable explanations of changed outcomes and potential policy ownership implications. A textual diff alone confuses renumbering with substantive change.

## Product requirements
Align Core outcomes using NIST crosswalk relationships, detect changed/unchanged wording and unmapped addition/removal candidates, preserve split/merge cardinality, explain possible organisational impact and produce a reviewer-approved register. Full narrative sections are a documented manual extension, not silently claimed automated coverage.

## Architecture
NIST CSF 1.1/2.0 Core exports + NIST crosswalk → versioned outcome inventory → many-to-many alignment → textual change classification → possible organisational impact → citations to both versions → reviewed change register. Python owns source parsing, stable identifiers, candidate records and validations. An optional local LLM only adds bounded explanations with exact quotations. A separate reviewer attests to the final content hash before export.

## Scope and constraints
A document/version change intelligence product, distinct from detection, vulnerability scoring, phishing, SOC analytics and compliance certification. It does not determine whether an organisation complies with a law or framework. Crosswalk relationships are not equivalence.

Source: NIST CSF 1.1 (2018), CSF 2.0 (2024), their Core exports and the 2024-02-20 NIST crosswalk. No large raw data commits. Standard-library baseline runs offline after checkout; source acquisition and optional model download require a connection once.

## Failure handling
Malformed input, duplicate IDs, absent source evidence, wrong source inventories and unknown citations fail closed. Do not repair missing facts using model guesses. Record exclusions and source/parser errors in the run report. Keep previous runs immutable for comparison.
