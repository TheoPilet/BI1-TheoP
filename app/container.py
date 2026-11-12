"""Composition root: the only place that wires the layers together.

Controllers ask for their dependencies with Depends(); the functions below decide
which concrete implementation is provided (e.g. an infrastructure client that
implements a port defined in application/ports).
"""

from app.application.services.health_service import HealthService


def get_health_service() -> HealthService:
    return HealthService()
