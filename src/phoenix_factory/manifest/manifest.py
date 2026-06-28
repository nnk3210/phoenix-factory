"""
Phoenix Manifest Model
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class Manifest:

    asset_id: str

    name: str

    category: str

    part: str

    path: str

    width: int

    height: int

    transparent: bool = True

    tags: list[str] = field(default_factory=list)