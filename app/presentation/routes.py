from fastapi import APIRouter

from app.presentation.controllers import health_controller

api_router = APIRouter()
api_router.include_router(health_controller.router)
