# Source register

| Local raw filename | Version/attribution | Acquisition URL |
|---|---|---|
| csf11.xlsx | NIST CSF 1.1 Core | https://www.nist.gov/document/2018-04-16frameworkv11core1xlsx |
| csf20.xlsx | NIST CSF 2.0 Reference Tool export; endpoint currently returns XLSX despite JSON in URL | https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all |
| crosswalk.xlsx | NIST CSF 1.1 to 2.0 crosswalk, 2024-02-20 | https://csrc.nist.gov/csrc/media/Projects/olir/documents/submissions/CSFv1.1_to_CSFv2.0_CROSSWALK_20240220.xlsx |

Source location checked 2026-10-17. Actual baseline hashes/bytes are in `metadata/baseline_manifest.json`; future downloads record their own acquisition UTC and hashes. A URL alone does not freeze content. Compare manifests and inspect release changes before replacing a cohort.

AMI: attribute the AMI Meeting Corpus and follow CC BY 4.0 for manual annotations 1.6.2. Do not confuse older mirror licences with this release. See https://groups.inf.ed.ac.uk/ami/download/ .

MITRE: credit The MITRE Corporation, retain source terms and ATT&CK attribution; see https://github.com/mitre-attack/attack-stix-data/blob/master/LICENSE.txt . Frozen 17.1 is intentionally selected, not claimed to be latest. Scenario records authored for this repository are synthetic.

NIST: retain NIST attribution and publication identifiers. Durable documents: CSF 1.1 https://doi.org/10.6028/NIST.CSWP.04162018 and CSF 2.0 https://doi.org/10.6028/NIST.CSWP.29 . Core exports and crosswalk are machine-readable aids; do not substitute them for publication-level interpretation. The reference tool endpoint may return XLSX despite its URL and can change; parser count guards and SHA-256 detect drift. Exclude third-party informative-reference text from derived Core fixtures.

No licence is granted here over third-party sources. Source register entries relevant to this project are identified by the acquisition table; cross-project resource notes are provided to prevent inconsistent team reuse.
