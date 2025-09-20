# AGENTS.md
Build/Lint/Test Commands
- Build: install dev deps and, if possible, build artifacts.
- Test: `pytest -q` (full suite); single test: `pytest backend/test/test_recipe.py::test_example -q`.
- Lint/Format: `ruff check .`, `ruff format --check .`, `black --check .`, `isort --check-only .`.
Code Style Guidelines
- **Imports**: standard, third-party, local; blank lines between groups; no wildcard imports.
- **Formatting**: follow Black (88 chars); auto-format where possible.
- **Types**: explicit hints; prefer `list[T]` and `A | B`; Python 3.13 unions allowed.
- **Naming**: snake_case for functions/vars; PascalCase for classes; ALL_CAPS for constants.
- **Error Handling**: raise precise exceptions; avoid bare except; log context.
- **Docs**: docstrings for modules/classes/functions; describe inputs/outputs.
- **Testing**: deterministic tests; isolate IO/DB; fixtures; avoid global state.
- **DB/IO**: use context managers; tests can override DB path via env var.
- **Versioning**: commit messages explain why, not just what.
Cursor Rules
- Cursor rules: none detected.
Copilot Rules
- Copilot rules: follow repo style; avoid credentials; keep changes minimal.
End