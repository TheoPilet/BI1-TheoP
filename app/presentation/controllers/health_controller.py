from typing import Annotated

from fastapi import APIRouter, Depends

from app.application.services.health_service import HealthService
from app.container import get_health_service
from app.presentation.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health check",
    description="Returns `ok` when the service is running.",
)
def health_check(
    service: Annotated[HealthService, Depends(get_health_service)],
) -> HealthResponse:
    return HealthResponse(status=service.get_status())
