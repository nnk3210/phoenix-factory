"""
Phoenix Module
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Module:

    name: str

    version: str

    enabled: bool = True