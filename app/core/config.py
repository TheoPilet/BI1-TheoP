from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings, read from environment variables.

    ENVIRONMENT=dev   -> API documentation (/docs, /openapi.json) is available
    ENVIRONMENT=prod  -> API documentation is disabled (default)
    """

    environment: Literal["dev", "prod"] = "prod"


settings = Settings()
