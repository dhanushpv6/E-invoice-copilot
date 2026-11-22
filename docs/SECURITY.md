# Security checklist

Status of each item at this snapshot. Unchecked means not implemented yet, not "not needed".

- [x] Secrets only via environment variables; `.env` is git-ignored, `.env.example` contains no secrets
- [x] Redacting log filter for e-mail, IBAN, phone and VAT-id patterns (`app/core/logging.py`)
- [ ] Upload type, signature and size checks (week 2)
- [ ] Treat OCR text and LLM output as untrusted (weeks 2 to 3)
- [ ] Authentication and role-based access (week 5)
- [ ] Malware scanning, rate limiting, retention and deletion policy (not implemented in this repo; required before real use)
