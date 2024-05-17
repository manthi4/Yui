from abc import ABC, abstractmethod


class Tool(ABC):
    """What counts as a tool anyway?"""

    @abstractmethod
    def call(self, input):
        """Calls the tool?"""
        pass
