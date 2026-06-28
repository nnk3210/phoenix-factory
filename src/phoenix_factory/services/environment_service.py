"""
Environment Service
"""

from phoenix_factory.config import Environment


class EnvironmentService:

    @staticmethod
    def all():

        return Environment.info()