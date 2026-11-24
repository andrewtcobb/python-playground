# microservice

FastAPI service managed with [uv](https://docs.astral.sh/uv/), linted/formatted with ruff, type-checked with ty.

```sh
uv sync                                   # install deps
uv run fastapi dev src/microservice/main.py   # dev server (http://127.0.0.1:8000/docs)
uv run pytest                             # tests
uv run ruff check . && uv run ruff format --check .
uv run ty check
```
