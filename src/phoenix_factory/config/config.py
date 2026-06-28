"""
Phoenix Factory Configuration
"""

from pathlib import Path


class Config:
    """Phoenix Factory 全域設定"""

    # 專案根目錄
    PROJECT_ROOT = Path(__file__).resolve().parents[3]

    # Assets
    ASSETS_DIR = PROJECT_ROOT / "assets"

    # Documents
    DOCS_DIR = PROJECT_ROOT / "docs"

    # Templates
    TEMPLATES_DIR = PROJECT_ROOT / "templates"

    # Schemas
    SCHEMAS_DIR = PROJECT_ROOT / "schemas"

    # Tests
    TESTS_DIR = PROJECT_ROOT / "tests"

    # Output
    OUTPUT_DIR = PROJECT_ROOT / "output"

    # Cache
    CACHE_DIR = PROJECT_ROOT / ".cache"

    # Logs
    LOG_DIR = PROJECT_ROOT / "logs"

    @classmethod
    def initialize(cls):
        """建立必要資料夾"""

        folders = [
            cls.OUTPUT_DIR,
            cls.CACHE_DIR,
            cls.LOG_DIR,
        ]

        for folder in folders:
            folder.mkdir(parents=True, exist_ok=True)