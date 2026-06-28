"""
Asset Pipeline
"""

from phoenix_factory.logging import Logger

from phoenix_factory.pipelines.pipeline import Pipeline

from phoenix_factory.paal import PAALLoader


class AssetPipeline(Pipeline):

    def __init__(self):

        self.logger = Logger()

    def execute(self):

        self.logger.info("Pipeline Started")

        paal = PAALLoader.load(
            "assets/character/hero/hero.paal.yaml"
        )

        self.logger.success("PAAL Loaded")

        print()

        self.logger.info(f"Asset ID   : {paal.asset_id}")

        self.logger.info(f"Name       : {paal.asset_name}")

        self.logger.info(f"Category   : {paal.category}")

        self.logger.info(f"Race       : {paal.race}")

        self.logger.info(f"Gender     : {paal.gender}")

        self.logger.info(f"Type       : {paal.asset_type}")

        self.logger.info(f"Part       : {paal.part}")

        self.logger.info(f"Canvas     : {paal.canvas}")

        self.logger.info(f"Resolution : {paal.width} x {paal.height}")

        print()

        self.logger.success("Pipeline Finished")