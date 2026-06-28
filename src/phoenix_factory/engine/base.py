"""
Project Phoenix Factory

Engine Base
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class Engine(ABC):
    """
    Base class for all Phoenix engines.
    """

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        """
        Engine name.
        """
        return self._name

    @abstractmethod
    def initialize(self) -> bool:
        """
        Initialize engine.

        Returns
        -------
        bool
            True if initialized successfully.
        """
        raise NotImplementedError

    @abstractmethod
    def shutdown(self) -> None:
        """
        Shutdown engine.
        """
        raise NotImplementedError