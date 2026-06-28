"""
Project Phoenix Factory
Version Information
"""

__title__ = "Project Phoenix Factory"
__version__ = "0.4.0"
__author__ = "Project Phoenix Architecture Team"
__license__ = "MIT"


def get_version() -> str:
    """Return current Phoenix Factory version."""
    return __version__


def get_application_name() -> str:
    """Return application name."""
    return __title__