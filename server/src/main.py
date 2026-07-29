"""FastAPI application entry point.

Run from the server/ directory:
    uvicorn src.main:app --reload --port 8000
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes.health import health_router
from src.core.config import get_app_settings

API_V1_PREFIX = "/api/v1"
API_TITLE = "MSK Lead Research API"
API_VERSION = "0.1.0"


def create_application() -> FastAPI:
    settings = get_app_settings()
    application = FastAPI(title=API_TITLE, version=API_VERSION, docs_url="/docs")
    application.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.frontend_origin],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(health_router, prefix=API_V1_PREFIX)
    return application


app = create_application()
