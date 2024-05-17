from Yui_core.Yui_IO import YuiInput


class ChatHistory(YuiInput):
    """Represent the common chathistory input type"""

    def to_string(self, llm_signature: str):
        """Returns chat history formatted in the approppriate format for the current LLM"""
        pass
