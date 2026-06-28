"""
Phoenix Factory Logger
"""

from .formatter import format_message
from .level import LogLevel
from .file_logger import FileLogger


class Logger:

    def __init__(self):

        self.file_logger = FileLogger()

    def _write(self, level, message):

        text = format_message(level, message)

        print(text)

        self.file_logger.write(text)

    def info(self, message):

        self._write(LogLevel.INFO, message)

    def success(self, message):

        self._write(LogLevel.SUCCESS, message)

    def warning(self, message):

        self._write(LogLevel.WARNING, message)

    def error(self, message):

        self._write(LogLevel.ERROR, message)