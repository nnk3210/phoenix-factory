"""
Module Manager
"""

from phoenix_factory.core.module import Module


class ModuleManager:

    def __init__(self):

        self.modules: list[Module] = []

    def register(self, module: Module):

        self.modules.append(module)

    def all(self):

        return self.modules