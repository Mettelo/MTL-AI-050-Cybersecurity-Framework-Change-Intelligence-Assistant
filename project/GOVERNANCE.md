# Governance and human review

## Main risks
False equivalence, missed split/merge relationships, dynamic reference exports, overconfident impact statements and invented legal obligations. Freeze hashes and retain publication identifiers; treat organisational impact as a hypothesis.

## Controls
- Source content and embedded instructions are untrusted data. Never execute them or treat them as approval.
- Local inference only; do not send transcripts, logs or organisation profiles to hosted APIs.
- Preserve observations, interpretations and recommendations separately. A valid quote may still support the wrong interpretation.
- Do not invent missing owners, dates, incident outcomes, framework obligations or certainty scores.
- A reviewer examines source evidence and all linked AI proposals, then accepts/rejects every record with reasons.
- Approval is bound to the complete draft SHA-256. Any correction requires renewed review.
- The local review file is an audit aid, not authenticated identity or tamper-proof access control. Use team repository permissions for accountability.
- Export is a file only. No messages, assignments, live response actions or policy updates occur automatically.

## Data management
Use the public frozen resources or approved synthetic data. Real internal data requires the organisation's lawful authority, minimisation and retention policy. Redact personal data, credentials and sensitive network identifiers. Keep raw sources and model caches outside version control. Reviewers define retention for private runs; delete when no longer needed. Preserve public-source attribution and applicable licence terms.

## Release gate
Domain reviewer signs factual accuracy; QA signs reproducibility and evaluation; delivery lead records remaining defects and approves release. A failed quality target is reported as failed, not waived by a successful demo.
