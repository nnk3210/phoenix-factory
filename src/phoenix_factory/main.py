"""
Project Phoenix Factory

Main Entry
"""

from phoenix_factory.core.bootstrap import Bootstrap


def main() -> None:
    """
    Phoenix Factory entry point.
    """
    Bootstrap.start()


if __name__ == "__main__":
    main()