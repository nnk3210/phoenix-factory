"""
Project Phoenix Factory

Application Entry
"""

from phoenix_factory.core.version import (
    get_application_name,
    get_version,
)


class PhoenixApplication:
    """
    Phoenix Factory Main Application.
    """

    def __init__(self) -> None:
        self.name = get_application_name()
        self.version = get_version()

    def run(self) -> None:
        """
        Start Phoenix Factory.
        """

        print("=" * 40)
        print(f"{self.name}")
        print("=" * 40)
        print(f"Version : {self.version}")
        print()
        print("Initializing...")
        print()
        print("✓ Config")
        print("✓ Logger")
        print("✓ Environment")
        print("✓ Asset Library")
        print("✓ Manifest")
        print("✓ PAAL")
        print("✓ Pipeline")
        print()
        print("Factory Ready.")