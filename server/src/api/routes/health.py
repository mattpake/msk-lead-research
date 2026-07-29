"""Liveness probe — confirms the API process is up and reports its environment."""

from fastapi import APIRouter

from src.core.config import get_app_settings

health_router = APIRouter(tags=["health"])


@health_router.get("/health")
async def check_service_health() -> dict[str, str]:
    settings = get_app_settings()
    return {
        "status": "ok",
        "service": "msk-lead-research-api",
        "environment": settings.app_env,
    }
