from abc import ABC, abstractmethod

from Yui_IO import YuiInput, YuiOutput


class Block(ABC):
    """Abstract class defining the fundemental building blocks of an application."""

    def __init__(
        self,
        input_types,
        output_types,
    ):
        """Initialize the block"""
        self.input_types = input_types
        self.output_types = output_types

    def input_checks(self, inputs: list[YuiInput]) -> list[YuiInput]:
        """Check if the received inputs are valid

        Args:
            inputs (list[YuiInput]): Block inputs

        Returns:
            list[YuiInput]: validated inputs
        """
        raise NotImplementedError()

    def output_checks(self, outputs: list[YuiOutput]) -> list[YuiOutput]:
        """Check if the outputs are valid

        Args:
            outputs (list[YuiOutput]): raw outputs

        Returns:
            list[YuiOutput]: validated outputs
        """
        raise NotImplementedError()

    @abstractmethod
    def forward(self, inputs: list[YuiInput]) -> list[YuiOutput]:
        """Run the inputs through the block to generate output

        Inputs will be validated before calling forward, outputs will be validated after.

        Args:
            inputs (list[YuiInput]): validated block inputs

        Returns:
            list[YuiOutput]: block outputs
        """
        pass
