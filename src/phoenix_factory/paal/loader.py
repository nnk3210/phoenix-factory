"""
PAAL Loader
"""

from pathlib import Path

import yaml

from phoenix_factory.paal.model import PAAL


class PAALLoader:

    @staticmethod
    def load(file_path: str) -> PAAL:

        path = Path(file_path)

        with open(path, "r", encoding="utf-8") as f:

            data = yaml.safe_load(f)

        return PAAL(

            version=data["version"],

            project=data["project"],

            asset_id=data["asset"]["id"],

            asset_name=data["asset"]["name"],

            category=data["asset"]["category"],

            race=data["asset"]["race"],

            gender=data["asset"]["gender"],

            asset_type=data["asset"]["type"],

            part=data["asset"]["part"],

            output=data["render"]["output"],

            background=data["render"]["background"],

            canvas=data["render"]["canvas"],

            color_space=data["render"]["color_space"],

            pivot=data["pivot"]["mode"],

            width=data["resolution"]["width"],

            height=data["resolution"]["height"],
        )