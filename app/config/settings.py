from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings, read from environment variables.

    ENVIRONMENT=dev   -> API documentation (/docs, /openapi.json) is available
    ENVIRONMENT=prod  -> API documentation is disabled (default)
    """

    model_config = SettingsConfigDict(env_file=".env")

    environment: Literal["dev", "prod"] = "prod"


settings = Settings()
