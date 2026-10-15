# Contributing

Contributions are welcome for bug fixes, tests, documentation, stream handling, export utilities, portability, and benchmarking.

## Development setup

```powershell
git clone https://github.com/dewanshpandey04/aerial-surveillance-multi-object-tracking.git
cd aerial-surveillance-multi-object-tracking

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run the test suite before submitting changes:

```powershell
pytest -q
```

## Workflow

1. Create a branch from `develop`.
2. Use a clear branch name such as `feature/...`, `fix/...`, or `docs/...`.
3. Keep commits focused and easy to review.
4. Add or update tests for reusable logic.
5. Run `pytest -q` before opening a pull request.
6. Open the pull request into `develop` and describe what changed and how it was validated.

## Code guidelines

- Target Python 3.11 or newer.
- Keep stream acquisition, inference, metadata, export, and metrics separated.
- Add type hints for reusable data structures and interfaces.
- Keep runtime settings configurable.
- Never expose credentials in logs, examples, or committed configuration.

## Repository boundaries

Do not commit private footage, customer data, stream credentials, proprietary datasets, production model weights, internal network details, or confidential deployment configuration.

## Branches

- `main` — stable branch
- `develop` — active development and integration
- `docs` — documentation work
