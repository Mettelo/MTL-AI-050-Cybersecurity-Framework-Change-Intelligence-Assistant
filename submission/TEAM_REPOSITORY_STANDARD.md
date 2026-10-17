# Team repository standard

Use a team-owned repository named `MTL-AI-050-<team-name>`. Link the upstream Mettelo project and retain source attribution. Keep the full project/data/submission pack, application, tests, evaluation and small reference fixtures.

Maintain a clear root README with setup, reproducible commands, business value, architecture, team roles, data/source restrictions, example outputs and known limitations. Use feature branches and reviewed pull requests, meaningful commits and a release tag. Record role contributions; combining roles does not remove independent review requirements.

Required folders: `project/`, `data/raw/`, `data/reference/`, `data/metadata/`, `tests/`, `scripts/`, `evaluation/`, `submission/`. Use ignored `runs/` locally. Final evidence may be copied into `submission/evidence/` after privacy review. Do not commit raw archives, weights, secrets, virtual environments or personal/internal telemetry.

Each PR must explain user-visible change, tests, grounding risks and data/model changes. A release must state the exact commit, Python version, source hashes and evaluated model digest. Keep gold splits immutable after lock.
