"""
PAAL Builder
"""

from phoenix_factory.models import Asset
from phoenix_factory.paal.model import PAAL


class PAALBuilder:

    @staticmethod
    def build(asset: Asset) -> PAAL:

        return PAAL(
            version="v1.0 Enterprise",
            project="Project Phoenix",
            asset_name=asset.name,
            category=asset.category,
            part=asset.part,
            output="PNG",
            background="Transparent",
            canvas="Tight Crop",
            pivot="Center",
            view="Front",
            style="Chibi Fantasy RPG",
        )