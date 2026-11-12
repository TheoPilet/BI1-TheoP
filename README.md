# BI1 Project

## Description
This repository contains my first version of a micro-service, built as part of
the SI-T2a BI1. The class project consists of implementing an
[ETL](https://aws.amazon.com/compare/the-difference-between-etl-and-elt/)
using a
[microservices-oriented architecture](https://aws.amazon.com/microservices/). Each student is responsible for a micro-service.

This first version is a REST API built with **Python** and **FastAPI**, managed with **uv**. The routes are covered by automated tests, and provides auto-generated Swagger/OpenAPI documentation: the routes can be consulted at `/docs` (dev environment only).

## Technology choice
| Item | Choice | Why |
| --- | --- | --- |
| Language | Python | Widely used in data / BI / ETL |
| Framework | FastAPI | Async, type hints, built-in validation, auto-generated OpenAPI docs |
| Package manager | uv | Fast, handles Python versions, virtualenv and lockfile in one tool |
| Tests | pytest + httpx | Standard for FastAPI (`TestClient`) |
| API documentation | Swagger UI (built into FastAPI) | Auto-generated from code at `/docs` (dev only) |
| Linter / formatter | Ruff | Fast, replaces flake8, isort and black in one tool |
| Type checking | mypy (strict) | Static type checking, same result in the terminal and in VS Code |
| Configuration | pydantic-settings | Reads settings (such as `ENVIRONMENT`) from environment variables, typed and validated |

### Resources studied
- [FastAPI – First steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI – Bigger applications (APIRouter)](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [FastAPI – Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [FastAPI – Metadata and docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/)
- [uv – Working on projects](https://docs.astral.sh/uv/guides/projects/)
- [pytest documentation](https://docs.pytest.org/en/stable/)
- [Ruff documentation](https://docs.astral.sh/ruff/)
- [mypy documentation](https://mypy.readthedocs.io/)
- [pydantic-settings documentation](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [VS Code – Python debugging](https://code.visualstudio.com/docs/python/debugging)
- [VS Code – Python testing](https://code.visualstudio.com/docs/python/testing)

## Getting Started
### Prerequisites
| Tool / Link | Minimal Version | What is it for? |
| --- | --- | --- |
| [Python](https://www.python.org/downloads/) | 3.13 | Language runtime (can be installed by uv) |
| [uv](https://docs.astral.sh/uv/getting-started/installation/) | 0.9 | Package and project manager |
| [VS Code](https://code.visualstudio.com/download) | v1.108.2 | IDE used |
| [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) | latest | VS Code extension for running, testing and managing Python environments |
| [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) | latest | Language server: IntelliSense, navigation and type checking |
| [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy) | latest | Debugging support (breakpoints, step-through) |
| [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) | latest | Linter and formatter used by the project |
| [Mypy Type Checker](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker) | latest | Static type checking in strict mode (uses the project's mypy) |
| [Fedora](https://www.fedoraproject.org/kde/download/) | 44 | Local dev machine |

Install uv on Linux/macOS:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Configuration
Copy the example environment file and adapt it if needed:
```bash
cp .env.example .env
```

| Variable | Values | Description |
| --- | --- | --- |
| `ENVIRONMENT` | `dev` or `prod` (default `prod`) | `dev` enables the API documentation (`/docs`, `/redoc`, `/openapi.json`) |
| `HOST` | IP address (default `127.0.0.1`) | Address the server listens on (used by `app.main.server`) |
| `PORT` | integer (default `8000`) | Port the server listens on (used by `app.main.server`) |


## Deployment
### On dev environment
#### Clone
```bash
git clone git@github.com:TheoPilet/BI1-TheoP.git
cd BI1-TheoP
```

#### Init
Creates the virtual environment and installs all dependencies from `uv.lock`:
```bash
uv sync
```

#### Run
The mode is chosen with the `ENVIRONMENT` variable (`dev` or `prod`, default `prod`), read from the `.env` file (see [Configuration](#configuration)). It controls the API documentation: `/docs`, `/redoc` and `/openapi.json` are only available in `dev`.

Development mode, reloads automatically when a file is saved, documentation enabled:
```bash
uv run fastapi dev app/main/app.py
```

Normal mode, without auto-reload and without documentation (as in production). The variable in the command overrides the `.env` file. After a code change, stop the server with `Ctrl+C` and start it again:
```bash
ENVIRONMENT=prod uv run python -m app.main.server
```

#### Tests
```bash
uv run pytest
```

Once running:
- Health check: http://127.0.0.1:8000/health
- Swagger UI (dev only): http://127.0.0.1:8000/docs
- OpenAPI schema (dev only): http://127.0.0.1:8000/openapi.json

#### debug
.vscode/launch.json
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "FastAPI: Debug",
      "type": "debugpy",
      "request": "launch",
      "module": "app.main.server",
      "args": [],
      "justMyCode": true
    }
  ]
}
```
1. Select the interpreter of the project (`Ctrl+Shift+P` -> *Python: Select Interpreter* -> `bi1-theop .venv/bin/python`)
2. Set a breakpoint (for example in `app/presentation/controllers/health_controller.py`)
3. Run and Debug -> *FastAPI: Debug*
4. Call http://127.0.0.1:8000/health, the execution stops on the breakpoint

#### tests
.vscode/settings.json
```json
{
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.testing.pytestArgs": ["tests"]
}
```
Tests can also be run and debugged from the VS Code *Testing* panel. The settings above make VS Code use pytest on the `tests/` folder.

#### Linter and formatter
The project uses [Ruff](https://docs.astral.sh/ruff/) as linter and formatter. It is installed as a dev dependency (`uv add --dev ruff`).

Check the code:
```bash
uv run ruff check .
```

Fix the issues automatically when possible:
```bash
uv run ruff check --fix .
```

Check or apply the formatting:
```bash
uv run ruff format --check .
uv run ruff format .
```

In VS Code, install the [Ruff extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff). The `.vscode/settings.json` file already makes Ruff the formatter for Python files, formats on save and applies the safe fixes and import sorting:
```json
{
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports.ruff": "explicit"
    }
  }
}
```

#### Type checking
The project enforces types with [mypy](https://mypy.readthedocs.io/) in strict mode. It is installed as a dev dependency (`uv add --dev mypy`) and configured in `pyproject.toml` (`[tool.mypy]`).

Check the types from the command line:
```bash
uv run mypy
```

In VS Code, the [Mypy Type Checker extension](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker) reports the same errors in the editor. Pylance is also set to `strict` in `.vscode/settings.json`:
```json
{
  "python.analysis.typeCheckingMode": "strict"
}
```

### On integration environment
_To be defined._

## Directory structure
The project is organized **by layer**, the same architecture for every ETL micro-service (extract, transform, load or data warehouse). It is inspired by the structure given in class.

```bash
.
├── .vscode/
├── app/
│   ├── main/
│   │   ├── app.py                    # FastAPI app creation, router registration
│   │   └── server.py                 # Starts the server (depends only on app.py)
│   ├── container.py                  # Composition root: wires the layers together (Depends)
│   ├── config/
│   │   └── settings.py               # Settings / environment configuration
│   ├── presentation/                 # PUBLIC: what the other micro-services can call
│   │   ├── routes.py                 # Groups all the controllers' routers
│   │   ├── controllers/
│   │   │   └── health_controller.py  # GET /health
│   │   └── schemas/                  # Pydantic models (API input / output)
│   ├── application/                  # PRIVATE: the work done to answer a request
│   │   ├── services/                 # Business logic / orchestration (no HTTP)
│   │   └── ports/                    # Interfaces needed from the outside world
│   ├── domain/                       # Business entities and rules
│   ├── infrastructure/               # Calls to the other micro-services
│   │   └── clients/                  # Adapters implementing the application ports
│   └── shared/                       # Helpers and utils used by all layers
├── tests/
├── pyproject.toml
├── uv.lock
└── README.md
```

| Layer | Role |
| --- | --- |
| `presentation/` | Exposed to the other micro-services: receives the request, validates it, delegates to the application |
| `application/` | Private part: does the work to answer the request. Defines the *ports* (interfaces) it needs |
| `domain/` | Entities and business rules, independent from everything else |
| `infrastructure/` | Fetches what is needed from the other micro-services (HTTP clients, storage...) by implementing the ports |
| `container.py` | Chooses which infrastructure implementation is given to the application |
| `config/` | Configuration read from environment variables |
| `shared/` | Cross-cutting helpers |

Dependency rule: `presentation` -> `application` -> `domain`. `infrastructure` implements the ports of `application`, and only `container.py` knows both sides.

> Most folders are empty for now: `/health` only needs a controller and a small service. They will be filled once the part of the ETL given to this micro-service is known.

## Collaborate
To collaborate with us, please:
  * If you want to propose a new feature, please create a new issue
  * Always respect the official [conventional commits norms](https://www.conventionalcommits.org/en/v1.0.0/)
  * Always [use your branching workflow correctly](https://nvie.com/posts/a-successful-git-branching-model/)

## License
This project is licensed under the MIT License.

## Contact
Théo Pilet
- Mail: theo.pilet@eduvaud.ch