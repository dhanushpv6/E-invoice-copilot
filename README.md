# E-Invoice Copilot: 

**Author:** Dhanush  


E-Invoice Copilot is a document-AI project that will turn PDF invoices into
standards-conformant German e-invoices (XRechnung, UBL), validate them, explain validation
errors in plain English and route uncertain results to a human reviewer.


## What this snapshot contains

- FastAPI application with `GET /health` and `GET /api/v1/invoices/capabilities`
- Environment-based settings (`app/core/config.py`, `.env.example`)
- Logging that masks e-mail addresses, IBANs, phone numbers and VAT ids (`app/core/logging.py`)
- Invoice domain schema aligned with EN 16931 business terms (`app/models/invoice.py`)
- Job status vocabulary (`app/models/jobs.py`)
- Tests and a GitHub Actions workflow (ruff and pytest on Python 3.11 and 3.12)
- Docs: architecture, roadmap, decisions, security checklist, evaluation plan, status

## Quick start

Requires Python 3.11 or newer.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
pytest
ruff check app tests
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs.

## Layout

```text
app/
  api/            HTTP routes
  core/           settings, logging
  models/         invoice schema, job statuses
tests/            pytest suite
docs/             architecture, roadmap, decisions, security, evaluation plan, status
```

## Dependency pinning

Dependencies use bounded version ranges in `pyproject.toml`. After your first successful
install, record exact versions (`pip freeze > requirements.lock`) and commit that file, since
LLM and PDF tooling changes quickly.

## License

MIT. Copyright (c) 2026 Dhanush.
