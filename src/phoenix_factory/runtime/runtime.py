"""
Project Phoenix Factory

Runtime
"""

from __future__ import annotations

from phoenix_factory.engine import EngineManager
from phoenix_factory.runtime.state import RuntimeState


class PhoenixRuntime:
    """
    Phoenix Runtime.
    """

    def __init__(self) -> None:
        self._state = RuntimeState.CREATED
        self._engine_manager = EngineManager()

    @property
    def state(self) -> RuntimeState:
        return self._state

    @property
    def engine_manager(self) -> EngineManager:
        return self._engine_manager

    def initialize(self) -> None:
        self._state = RuntimeState.INITIALIZING

        self._engine_manager.initialize_all()

        self._state = RuntimeState.READY

    def shutdown(self) -> None:
        self._engine_manager.shutdown_all()

        self._state = RuntimeState.STOPPED