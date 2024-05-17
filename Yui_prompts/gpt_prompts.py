from Yui_core.chat_history import ChatHistory
from Yui_core.prompt import LlmID, YuiPrompt


class BasicPrompt(YuiPrompt):
    """A basic prompt, doesn't do much"""

    def __init__(self, llm: LlmID):
        """Initialize basic prompt"""
        super().__init__(llm)


class ReactPrompt(YuiPrompt):
    """Basic react prompt"""

    def target_llm(self):
        """Prompt's target llm"""
        return LlmID("gpt-3")

    def compile(self, inputs):
        """Send back finished prompt"""
        prompt = self._compile(
            chat_history=inputs["chat_history"], agent_scratchpad=inputs, tools=inputs
        )
        return prompt

    def _compile(self, chat_history: ChatHistory, agent_scratchpad: str, tools: list) -> str:
        """Compile inputs into a prompt string"""
        tool_desciptions = ""
        for tool in tools:
            tool_desciptions += f"{tool.description}\n"
        compiled_prompt = f"""system:
                You are a friendly assistant that is constantly learning. You speak curtly.
                Answer the following questions as best you can.
                You have access to the following tools:

                {tool_desciptions}
                Use the following format:

                Request: the input request you must answer
                Thought: you should always think about what to do
                Action: the action to take, should be to use of the tools
                Action Input: the input to the action
                Observation: the result of the actions
                ... (this Thought/Action/Action Input/Observation can repeat N times)
                Thought: I have responded to the request
                Final Answer: the final response to the original input
                Begin!

                {chat_history}

                {agent_scratchpad}
                """
        return compiled_prompt
