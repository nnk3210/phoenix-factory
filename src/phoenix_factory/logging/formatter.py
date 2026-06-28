from datetime import datetime

from .level import LogLevel


def format_message(level: LogLevel, message: str) -> str:
    now = datetime.now().strftime("%H:%M:%S")
    return f"[{now}] [{level.value}] {message}"