import os
from Yui_IO import YuiInputs, YuiOutputs
from prompt import YuiPrompt
from llm_interface import LlmInterface


class YuiBlock:

    def __init__(
        self,
        inputs: YuiInputs,
        prompt: YuiPrompt,
        llm: LlmInterface,
        outputs: YuiOutputs,
    ):
        self.inputs = inputs
        self.prompt = prompt
        self.llm = llm
        self.outputs = outputs

    def forward(self, inputs: list[YuiInputs]):
        compiled_prompt = self.prompt.compile(inputs)
        ### TODO: later we may have to pass in the outputs as well,
        ### if we want to do output validation at the log probs level
        raw_response = self.llm.call(compiled_prompt)
        response = self.outputs.parse(response)
        return response
