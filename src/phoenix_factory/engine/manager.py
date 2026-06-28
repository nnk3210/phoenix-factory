"""
Project Phoenix Factory

Engine Manager
"""

from __future__ import annotations

from typing import Dict

from phoenix_factory.engine.base import Engine


class EngineManager:
    """
    Manage all Phoenix engines.
    """

    def __init__(self) -> None:
        self._engines: Dict[str, Engine] = {}

    def register(self, engine: Engine) -> None:
        """
        Register an engine.

        Raises
        ------
        ValueError
            If the engine name already exists.
        """
        if engine.name in self._engines:
            raise ValueError(
                f"Engine '{engine.name}' already registered."
            )

        self._engines[engine.name] = engine

    def get(self, name: str) -> Engine:
        """
        Get engine by name.
        """
        return self._engines[name]

    def initialize_all(self) -> None:
        """
        Initialize all registered engines.
        """
        for engine in self._engines.values():
            engine.initialize()

    def shutdown_all(self) -> None:
        """
        Shutdown all registered engines.
        """
        for engine in reversed(list(self._engines.values())):
            engine.shutdown()

    @property
    def engines(self) -> Dict[str, Engine]:
        """
        Registered engines.
        """
        return dict(self._engines)