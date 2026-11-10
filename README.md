# BI1 Project

## Description
This repository contains my first version of a micro-service, built as part of
the SI-T2a BI1. The class project consists of implementing an
[ETL](https://aws.amazon.com/compare/the-difference-between-etl-and-elt/)
using a
[microservices-oriented architecture](https://aws.amazon.com/microservices/). Each student is responsible for one or two micro-services.

This first version is a REST API built with **Python** and **FastAPI**, managed with **uv**. It exposes a `GET /health` route, is covered by automated tests, and provides auto-generated Swagger/OpenAPI documentation.

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
No configuration is required for this first version. The API listens on `http://127.0.0.1:8000` by default.

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
The mode is chosen with the `ENVIRONMENT` variable (`dev` or `prod`, default `prod`). It controls the API documentation: `/docs`, `/redoc` and `/openapi.json` are only available in `dev`.

Development mode, reloads automatically when a file is saved, documentation enabled:
```bash
ENVIRONMENT=dev uv run fastapi dev app/main.py
```

Normal mode, without auto-reload and without documentation (as in production). After a code change, stop the server with `Ctrl+C` and start it again:
```bash
ENVIRONMENT=prod uv run fastapi run app/main.py
```

Both commands serve the API on `http://127.0.0.1:8000`. The `/health` route is available in both modes.

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
      "module": "uvicorn",
      "args": ["app.main:app"],
      "justMyCode": true
    }
  ]
}
```
1. Select the interpreter of the project (`Ctrl+Shift+P` -> *Python: Select Interpreter* -> `bi1-theop .venv/bin/python`)
2. Set a breakpoint (for example in `app/routers/health.py`)
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
The project is organized **by file type**, following the layout recommended in the official FastAPI documentation: [Bigger Applications – Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/).

```bash
.
├── .vscode/
│   ├── launch.json
│   └── settings.json
├── app/
│   ├── main.py              # FastAPI app creation, router registration
│   ├── dependencies.py      # Shared dependencies (used with Depends())
│   ├── core/
│   │   └── config.py        # Settings / environment configuration
│   ├── routers/
│   │   └── health.py        # GET /health
│   ├── services/            # Business logic (no HTTP concerns)
│   ├── schemas/             # Pydantic models (API input / output)
│   └── models/              # Persistence models (database tables)
├── tests/
│   └── test_health.py       # Functional test of /health
├── pyproject.toml           # Project metadata and dependencies
├── uv.lock                  # Locked dependency versions
└── README.md
```

| Folder | Role |
| --- | --- |
| `routers/` | Controllers: receive the request, validate it, delegate to a service |
| `services/` | Business logic, independent from HTTP |
| `schemas/` | Pydantic schemas: the contract of the API |
| `models/` | Persistence models (database entities) |
| `core/` | Configuration and cross-cutting concerns |
| `tests/` | Automated tests (pytest) |

> `services/`, `schemas/` and `models/` are empty for now: `/health` check service health. They will be filled as the ETL micro-service grows.

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