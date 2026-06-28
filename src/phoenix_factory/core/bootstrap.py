"""
Project Phoenix Factory

Bootstrap
"""

from phoenix_factory.core.application import PhoenixApplication


class Bootstrap:
    """
    Bootstrap Phoenix Factory.
    """

    @staticmethod
    def start() -> None:
        """
        Start Phoenix Factory.
        """

        app = PhoenixApplication()
        app.run()