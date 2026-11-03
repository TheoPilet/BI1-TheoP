from fastapi import FastAPI

from app.routers import health

app = FastAPI(
    title="BI1 ETL micro-service",
    description="REST API of the BI1 ETL micro-service.",
    version="0.1.0",
)

app.include_router(health.router)
