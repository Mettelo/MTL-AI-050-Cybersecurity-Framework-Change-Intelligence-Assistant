# Data and exact acquisition

Primary resource: NIST CSF 1.1 (2018), CSF 2.0 (2024), their Core exports and the 2024-02-20 NIST crosswalk.

| Local raw filename | Resource/version | Exact URL |
|---|---|---|
| csf11.xlsx | NIST CSF 1.1 Core | https://www.nist.gov/document/2018-04-16frameworkv11core1xlsx |
| csf20.xlsx | NIST CSF 2.0 Reference Tool export; endpoint currently returns XLSX despite JSON in URL | https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all |
| crosswalk.xlsx | NIST CSF 1.1 to 2.0 crosswalk, 2024-02-20 | https://csrc.nist.gov/csrc/media/Projects/olir/documents/submissions/CSFv1.1_to_CSFv2.0_CROSSWALK_20240220.xlsx |

From the root, run `python scripts/fetch_sources.py`. This downloads into ignored `data/raw/` and creates `data/metadata/download_manifest.json` with URL, byte count, SHA-256 and access time. It reuses existing local files; explicitly remove/replace a file only when you intend to refresh it, then compare hashes and rerun validation. Never silently overwrite the frozen cohort.

Prepare using:
```text
python app.py prepare --source data/raw --output runs/framework.json
```

The bundled `data/reference/demo.json` is a small frozen input for offline reproduction. Its provenance is recorded in `data/metadata/baseline_manifest.json`. Never describe synthetic examples as real incidents or demo subsets as benchmark test sets.

Raw archives, complete STIX bundles, audio/video and model weights must not be committed. Commit only small derived fixtures, manifests, gold labels and scripts. Read [source register](SOURCE_REGISTER.md) before redistributing.
