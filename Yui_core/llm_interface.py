from abc import ABC, abstractmethod


class LlmInterface(ABC):
    """Abstract class to define an LlmInterface"""

    @abstractmethod
    def __init__(self):
        """Initialize LlmInterface"""
        pass

    @abstractmethod
    def call(self, prompt: str) -> str:
        """Take in the compiled prompt and run it through

        Args:
            prompt (str): compiled prompt

        Returns:
            str: model output
        """
        pass
