import time
import uuid

import structlog
from flask import Flask, Response, g, jsonify, request
from flask.typing import ResponseReturnValue

from python_microservice.logging import configure_logging

log = structlog.get_logger()


def create_app() -> Flask:
    configure_logging()
    app = Flask(__name__)

    @app.before_request
    def start_request() -> None:
        g.start = time.perf_counter()
        structlog.contextvars.clear_contextvars()
        structlog.contextvars.bind_contextvars(
            request_id=request.headers.get("X-Request-ID", str(uuid.uuid4())),
            method=request.method,
            path=request.path,
        )

    @app.after_request
    def log_request(response: Response) -> Response:
        log.info(
            "request_completed",
            status=response.status_code,
            duration_ms=round((time.perf_counter() - g.start) * 1000, 2),
        )
        return response

    @app.get("/health")
    def health() -> ResponseReturnValue:
        return jsonify(status="ok")

    @app.get("/hello")
    def hello() -> ResponseReturnValue:
        log.info("saying_hello")
        return jsonify(message="Hello, World!")

    return app
