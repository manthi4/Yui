from abc import ABC, abstractmethod
from typing import NewType

from Yui_core.Yui_IO import YuiInput

LlmID = NewType("LlmID", str)


class YuiPrompt(ABC):
    """An abstract method for prompts

    Each prompt should only target one specific llm.
    Prompts are inherently tied to the llm and task
    so users are encouraged to make custom prompts
    """

    def __init__(self, llm: LlmID):
        """Initialize prompt"""
        assert llm == self.target_llm

    @property
    @abstractmethod
    def target_llm(self) -> LlmID:
        """Define which llm this prompt targets"""
        pass

    @abstractmethod
    def compile(self, inputs: list[YuiInput]) -> str:
        """Encorporate inputs into the prompt

        Args:
            inputs (list[YuiInput]): The prompt's inputs

        Returns:
            str: the compiled prompt
        """
        pass
