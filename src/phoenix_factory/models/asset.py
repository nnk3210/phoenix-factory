"""
Phoenix Factory Asset Model
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Asset:
    """
    Phoenix Asset
    """

    name: str

    category: str

    part: str

    file: Path

    width: int = 0

    height: int = 0

    transparent: bool = True

    description: str = ""