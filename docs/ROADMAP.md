# Five-week implementation roadmap

Follows project 1 of the AI portfolio plan (about 15 to 20 hours per week).

| Week | Focus | Exit criteria |
|---|---|---|
| 1 | Repository, FastAPI, settings, logging, invoice schema, tests, CI | App starts; health and capabilities pass; CI green |
| 2 | Upload hardening, PDF text layer, OCR for scanned PDFs | Text and scanned PDFs take distinct, tested paths |
| 3 | LLM provider abstraction, extraction, grounding checks, XRechnung UBL XML | Structured extraction and deterministic XML tests |
| 4 | EN 16931 / XRechnung rule checks, KoSIT adapter, explanations, review queue, database | Validation result and review status are explicit and persisted |
| 5 | Model cascade, 50+ document evaluation, auth, UI, Docker, demo | Reproducible local MVP, measured results, documented failures |

## Scope rule

One output syntax only: XRechnung (UBL). Do not add a second format until one complete path
is validated.
