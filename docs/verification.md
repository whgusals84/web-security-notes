# Verification record

Executed locally on 2026-09-09 using Windows, CPython 3.13.2 / Node 25.0.0.

| Command | Result |
| --- | --- |
| `python -m pytest -q` | 14 passed in 0.05s |
| `python -m ruff check .` | Passed |
| `python -m ruff format --check .` | Passed |
| `python origins.py` | Passed |

Relative Markdown links resolved and the staged-source scan passed before publishing. Secret scanning uses
common token/private-key patterns and suspicious filenames; it is heuristic, not an audit.
Tests cover these fixtures and contracts, not general production security.

The scanner flagged the fixed `a:b` userinfo in a `.invalid` URL rejection test. It was
reviewed as a public synthetic fixture; no live credential is present.
