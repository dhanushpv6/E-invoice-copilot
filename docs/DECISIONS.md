# Architecture decision records

## ADR-001: Modular monolith
**Decision:** One FastAPI application with isolated service modules.
**Reason:** Small enough to build and test without microservice overhead; boundaries stay
explicit so a module can be split out later.

## ADR-002: Lenient invoice schema, strict rule checks
**Decision:** All invoice fields are optional; mandatory-field and arithmetic checks are
separate, explicit rules (week 4).
**Reason:** Extraction is lossy. A missing value should become a review task with a reason,
not an unhandled error, and wrong printed totals must be representable to be flagged.

## ADR-003: Log hygiene by construction
**Decision:** Log job ids, stages and counts only, plus a redacting filter for e-mail, IBAN,
phone and VAT-id patterns.
**Reason:** Invoices contain personal and financial data; logs must not become a copy of it.
