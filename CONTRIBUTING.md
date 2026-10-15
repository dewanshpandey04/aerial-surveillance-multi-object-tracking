# Contributing

Contributions are welcome for bug fixes, tests, documentation, stream handling, metadata processing, export utilities, portability, and benchmarking.

## Development setup

```powershell
git clone https://github.com/dewanshpandey04/aerial-surveillance-multi-object-tracking.git
cd aerial-surveillance-multi-object-tracking

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

Install `requirements.txt` as well when running the YOLO/OpenCV application locally.

## Quality checks

Before opening a pull request, run:

```powershell
python -m compileall -q src scripts tests
ruff check .
python -m pytest -q
```

## Workflow

1. Branch from `develop`.
2. Use a focused name such as `feature/...`, `fix/...`, or `docs/...`.
3. Keep each change scoped to one problem.
4. Add or update tests when reusable logic changes.
5. Run the local quality checks.
6. Open a pull request into `develop` and describe the change and validation performed.

## Code guidelines

- Support Python 3.10+.
- Keep stream handling, inference, metadata, export, and metrics separated.
- Use type hints for reusable interfaces and data structures.
- Normalize framework-specific results before using them in application logic.
- Keep sources, thresholds, model paths, and devices configurable.
- Never expose credentials in logs, examples, or committed configuration.
- Do not commit private footage, production weights, datasets, or confidential deployment settings.

## Branches

- `main` — stable branch
- `develop` — active development and integration
- `docs` — documentation work
