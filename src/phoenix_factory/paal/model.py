"""
PAAL Enterprise Model
"""

from dataclasses import dataclass


@dataclass(slots=True)
class PAAL:

    version: str

    project: str

    asset_id: str

    asset_name: str

    category: str

    race: str

    gender: str

    asset_type: str

    part: str

    output: str

    background: str

    canvas: str

    color_space: str

    pivot: str

    width: int

    height: int