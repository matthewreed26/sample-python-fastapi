# sample-python-fastapi DDD/BDD Rapid Prototype Scaffold

This repository provides a clean-architecture foundation for building scalable Python APIs. It isolates core business logic from framework dependencies and utilizes `uv` for lightning-fast, reproducible environment management.

## Project Architecture (DDD)

- **Domain Layer (`src/app/domain`)**: Pure Python dataclasses and protocol definitions. The absolute core of the business logic.
- **Application Layer (`src/app/application`)**: Orchestrates use cases using the domain models and infrastructure interfaces.
- **Infrastructure Layer (`src/app/infrastructure`)**: Concrete implementations of external concerns (e.g., In-Memory Database, SQLAlchemy).
- **API Layer (`src/app/api`)**: FastAPI application, Pydantic I/O boundaries, and dependency injection.

## Environment Setup & Execution

We rely exclusively on Astral's `uv` for package and environment management.

**1. Install dependencies:**

```bash
uv sync
```

**2. Run the development server:**

```bash
uv run uvicorn src.api.main:app --reload
```

The API documentation will be available at <http://127.0.0.1:8000/docs>.

**3. Run the test suite (BDD-Style with Coverage):**

```bash
uv run pytest
```

## Adding New Features

1. Define your new entity in domain/models.py.
2. Define the interface for data access in domain/ports.py.
3. Build the orchestration logic in application/services.py and write your tests/.
4. Implement the concrete data access in infrastructure/repositories.py.
5. Expose the functionality via api/routers.py.

## Resources & Reference Patterns

For looking up advanced patterns or extending this scaffold, refer to the following:

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/): Comprehensive guides on dependency injection and background tasks.
- [Architecture Patterns with Python (Cosmic Python)](https://www.cosmicpython.com/book/preface.html): The definitive guide to DDD, TDD, and Event-Driven architecture in Python.
- [Astral uv Documentation](https://docs.astral.sh/uv/): Reference for managing dependency locks, virtual environments, and python versions.
- [Pytest Mocking Guide](https://pytest-mock.readthedocs.io/en/latest/): Essential for isolating application logic during unit testing.
