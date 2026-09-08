# Web security notes

[![checks](https://github.com/whgusals84/web-security-notes/actions/workflows/ci.yml/badge.svg)](https://github.com/whgusals84/web-security-notes/actions/workflows/ci.yml)

**Origins, cookies, and request intent.**

브라우저가 무엇을 분리하고 무엇을 자동으로 보내는지 작은 예제로 구분합니다.

## Read and run

- [Implementation](origins.py) — small functions with explicit contracts.
- [Study guide](docs/browser-boundaries.md) — reasoning, examples, limitations, and review questions.
- [Tests](tests/) — expected behavior and boundary cases.

Python 3.11+, from this checkout. Create an environment with `python -m venv .venv`;
activate it with `.venv\Scripts\Activate.ps1` (PowerShell) or `source .venv/bin/activate` (POSIX).

```sh
python -m pip install -r requirements-dev.txt
python origins.py
python -m pytest
python -m ruff check .
python -m ruff format --check .
```

No network target or credential is accepted. Fixtures belong to this repository. The code is an
educational model, not a production security library, audit, or claim of completed coursework.

## Study loop

Predict an outcome, run the example, read the assertion, then explain the boundary in your own words.
Change one input and identify which invariant should still hold. A passing test only proves the
specific property it checks; document what remains outside the model.

[Verification](docs/verification.md) · [Repository history](docs/repository-history.md)
· [Contributing](CONTRIBUTING.md) · [MIT license](LICENSE)
