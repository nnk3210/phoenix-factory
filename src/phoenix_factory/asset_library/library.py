"""
Phoenix Asset Library
"""

from phoenix_factory.models import Asset


class AssetLibrary:

    def __init__(self):

        self._assets: list[Asset] = []

    def add(self, asset: Asset):

        self._assets.append(asset)

    def all(self):

        return self._assets

    def count(self):

        return len(self._assets)