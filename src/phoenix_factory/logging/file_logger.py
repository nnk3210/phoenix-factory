"""
Phoenix Factory File Logger
"""

from pathlib import Path
from datetime import datetime

from phoenix_factory.config import Config


class FileLogger:

    def write(self, message: str):

        Config.initialize()

        log_file = Config.LOG_DIR / "phoenix.log"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")