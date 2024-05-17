from llm_interface import LlmInterface
from prompt import YuiPrompt
from Yui_IO import YuiInput, YuiOutput

from Yui_core.Block import Block


class LlmBlock(Block):
    """A Block that encompasses an llm"""

    def __init__(
        self,
        inputs: list[YuiInput],
        prompt: YuiPrompt,
        llm: LlmInterface,
        outputs: list[YuiOutput],
    ):
        """Initialize the LlmBlock

        Args:
            inputs (list[YuiInput]): expected inputs
            prompt (YuiPrompt): the block's prompt
            llm (LlmInterface): _description_
            outputs (list[YuiOutput]): _description_
        """
        super().__init__(input_types=inputs, output_types=outputs)
        self.inputs = inputs
        self.prompt = prompt
        self.llm = llm
        self.outputs = outputs

    def forward(self, inputs: list[YuiInput]) -> list[YuiOutput]:
        """Make the llm call with given inputs

        Args:
            inputs (list[YuiInput]): validated? inputs

        Returns:
            list[YuiOutput]: unvalidated outputs
        """
        compiled_prompt = self.prompt.compile(inputs)
        # TODO: later we may have to pass in the outputs as well,
        # if we want to do output validation at the log probs level
        raw_response = self.llm.call(compiled_prompt)
        print(raw_response)

        res = YuiOutput()
        return res
