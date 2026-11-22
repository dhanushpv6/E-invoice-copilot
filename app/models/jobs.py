"""Job lifecycle vocabulary shared by the pipeline, the API and the UI."""


class JobStatus:
    UPLOADED = "uploaded"
    OCR_UNAVAILABLE = "ocr_unavailable"
    EXTRACTION_FAILED = "extraction_failed"
    EXTRACTED = "extracted"  # extraction done, no validation stage in this build
    NEEDS_REVIEW = "needs_review"
    LOCALLY_CHECKED = "locally_checked"  # local rules pass; official validator not configured
    ACCEPTED = "accepted"  # official validator accepted and no review reasons remain
    REJECTED = "rejected"  # a reviewer rejected the document

    ALL = (
        UPLOADED, OCR_UNAVAILABLE, EXTRACTION_FAILED, EXTRACTED,
        NEEDS_REVIEW, LOCALLY_CHECKED, ACCEPTED, REJECTED,
    )
