import uvicorn

from app.config.settings import settings
from app.main.app import app


def run() -> None:
    uvicorn.run(app, host=settings.host, port=settings.port)


if __name__ == "__main__":
    run()
