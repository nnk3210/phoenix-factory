"""
Phoenix Factory Bootstrap
"""

from phoenix_factory.config import Config
from phoenix_factory.logging import Logger


class Bootstrap:

    def __init__(self):

        self.logger = Logger()

    def initialize(self):

        Config.initialize()

        self.logger.info("Bootstrapping Phoenix Factory...")

        self.logger.success("Config Ready")

        self.logger.success("Logger Ready")

        self.logger.success("Environment Ready")