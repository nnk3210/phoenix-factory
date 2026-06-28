"""
Asset Service
"""

from pathlib import Path

from phoenix_factory.models import Asset
from phoenix_factory.asset_library import AssetLibrary


class AssetService:

    def __init__(self):

        self.library = AssetLibrary()

    def create_sample(self) -> Asset:

        asset = Asset(
            name="Hero",
            category="Character",
            part="Body",
            file=Path("assets/hero/body.png"),
            width=1024,
            height=1024,
            transparent=True,
        )

        self.library.add(asset)

        return asset

    def assets(self):

        return self.library.all()

    def count(self):

        return self.library.count()