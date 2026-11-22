from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(prefix="/api/v1", tags=["invoices"])


@router.get("/invoices/capabilities")
def capabilities() -> dict:
    """Report what this build can really do, so the UI and tests never over-claim."""
    return {
        "pdf_text_extraction": False,
        "ocr": False,
        "extraction": "none",
        "xml_generation": False,
        "local_rule_checks": False,
        "official_validation": False,
        "human_review_queue": False,
        "environment": settings.environment,
    }
