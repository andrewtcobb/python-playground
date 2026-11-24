# python-microservice

A simple Flask microservice using [uv](https://docs.astral.sh/uv/), [ruff](https://docs.astral.sh/ruff/) and [ty](https://docs.astral.sh/ty/).

```sh
uv sync                                   # install deps
uv run python -m python_microservice      # dev server on :5000
uv run gunicorn "python_microservice:create_app()"  # production server
uv run pytest                             # tests
uv run ruff check . && uv run ruff format --check .  # lint + format
uv run ty check                           # type check
```
