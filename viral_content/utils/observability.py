"""Opt-in structured logging helpers for production runs."""
import json
import logging
import os
import uuid


def request_id() -> str:
    return os.getenv("VIRAL_REQUEST_ID", uuid.uuid4().hex)


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        return json.dumps({"timestamp": self.formatTime(record, "%Y-%m-%dT%H:%M:%S%z"), "level": record.levelname, "logger": record.name, "message": record.getMessage(), "request_id": request_id()}, ensure_ascii=False)


def configure_json_logging() -> str:
    rid = request_id()
    if os.getenv("VIRAL_JSON_LOGS") == "1":
        for handler in logging.getLogger().handlers:
            handler.setFormatter(JsonFormatter())
    return rid
