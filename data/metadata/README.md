# Provenance and contracts

`resources.json`: official source URLs and expected filenames. `baseline_manifest.json`: hashes/byte counts used to construct the bundled input. `download_manifest.json`: generated locally, ignored. `input_schema.md`: domain input fields and semantics.

For final evaluation add `split_manifest.json` containing scenario/meeting/component IDs, split, source hash, label version, reviewer/adjudicator and lock date. Record model name/digest, prompt version, seed, temperature, context size, hardware, elapsed time and output hash in every AI experiment. No API keys belong in metadata.
