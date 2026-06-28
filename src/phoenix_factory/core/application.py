"""
Project Phoenix Factory

Application Entry
"""

from phoenix_factory.core.version import (
    get_application_name,
    get_version,
)

from phoenix_factory.runtime import PhoenixRuntime
from phoenix_factory.pipelines.asset_pipeline import AssetPipeline


class PhoenixApplication:
    """
    Phoenix Factory Main Application.
    """

    def __init__(self) -> None:

        self.name = get_application_name()

        self.version = get_version()

        self.runtime = PhoenixRuntime()

        self.pipeline = AssetPipeline()

    def run(self) -> None:

        print("=" * 40)

        print(self.name)

        print("=" * 40)

        print(f"Version : {self.version}")

        print()

        print("Initializing...")

        print()

        self.runtime.initialize()

        print("✓ Runtime Ready")

        print()

        self.pipeline.execute()

        print()

        print("Factory Ready.")