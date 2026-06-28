"""
Phoenix Runtime State
"""

from enum import Enum


class RuntimeState(str, Enum):
    CREATED = "CREATED"
    INITIALIZING = "INITIALIZING"
    READY = "READY"
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"