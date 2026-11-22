from fastapi import FastAPI

from app import __version__
from app.api.routes import router
from app.core.config import settings
from app.core.logging import configure_logging

configure_logging(settings.log_level)


app = FastAPI(title=settings.app_name, version=__version__)
app.include_router(router)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok", "environment": settings.environment}
