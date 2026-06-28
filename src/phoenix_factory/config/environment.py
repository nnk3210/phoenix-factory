"""
Phoenix Factory Environment
"""

from pathlib import Path


class Environment:

    ROOT = Path(__file__).resolve().parents[3]

    ASSETS = ROOT / "assets"

    OUTPUT = ROOT / "output"

    LOGS = ROOT / "logs"

    CACHE = ROOT / ".cache"

    DOCS = ROOT / "docs"

    SCHEMAS = ROOT / "schemas"

    TEMPLATES = ROOT / "templates"

    TESTS = ROOT / "tests"

    @classmethod
    def info(cls):

        return {
            "ROOT": cls.ROOT,
            "ASSETS": cls.ASSETS,
            "OUTPUT": cls.OUTPUT,
            "LOGS": cls.LOGS,
            "CACHE": cls.CACHE,
            "DOCS": cls.DOCS,
            "SCHEMAS": cls.SCHEMAS,
            "TEMPLATES": cls.TEMPLATES,
            "TESTS": cls.TESTS,
        }