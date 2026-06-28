"""
Manifest Service
"""

from phoenix_factory.manifest.manifest import Manifest
from phoenix_factory.models import Asset


class ManifestService:

    @staticmethod
    def from_asset(asset: Asset) -> Manifest:

        return Manifest(

            asset_id=f"{asset.category}_{asset.part}_{asset.name}",

            name=asset.name,

            category=asset.category,

            part=asset.part,

            path=str(asset.file),

            width=asset.width,

            height=asset.height,

            transparent=asset.transparent,
        )