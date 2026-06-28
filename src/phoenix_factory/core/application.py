from phoenix_factory.config import Config
from phoenix_factory.core.banner import print_banner
from phoenix_factory.logging import Logger
from phoenix_factory.pipelines import AssetPipeline


class PhoenixApplication:

    def start(self):

        logger = Logger()

        Config.initialize()

        print_banner()

        print("AI Asset Production Pipeline")
        print()

        logger.success("Framework Ready")

        print()

        pipeline = AssetPipeline()

        pipeline.execute()

        print()

        logger.success("Phoenix Factory Ready.")