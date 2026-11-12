class HealthService:
    """Answers the health check. The business work of the micro-service lives here."""

    def get_status(self) -> str:
        return "ok"
