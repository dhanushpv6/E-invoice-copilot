# Evaluation plan

Build a labelled set of at least 50 synthetic or openly licensed English invoices, including
hard cases: missing fields, mixed currencies, wrong totals, duplicates and poor scans. Keep a
development set and a locked test set separate and never tune on the test set.

Record, with date and model versions:

- Share passing validation without fixes, and after human review
- Field-level precision and recall (invoice number, dates, parties, currency, lines, totals)
- Cost per document and latency
- Top failure reasons by category

No number is published until it has been measured. Write the evaluation first (week 5 builds
the harness and dataset; earlier weeks only prepare the schema it needs).
