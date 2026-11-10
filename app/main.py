from fastapi import FastAPI

from app.core.config import settings
from app.routers import health

docs_enabled = settings.environment == "dev"

app = FastAPI(
    title="BI1 ETL micro-service",
    description="REST API of the BI1 ETL micro-service.",
    version="0.1.0",
    docs_url="/docs" if docs_enabled else None,
    redoc_url="/redoc" if docs_enabled else None,
    openapi_url="/openapi.json" if docs_enabled else None,
)

app.include_router(health.router)
