from chat_history import ChatHistory


class YuiPrompt:
    ###TODO: make this a abc class or pydantic object
    def compile(example_input: str):
        compiled_prompt = f"example prompt {example_input}"
        return compiled_prompt


############# Example prompt
class ReactPrompt(YuiPrompt):

    def __init__(self, llm: str):
        self.target_llm = (
            "gpt-3"  ### TODO: how to properly instantiate hard coded class variable
        )
        assert llm == self.target_llm

    def compile(self, chat_history: ChatHistory, agent_scratchpad: str, tools: list):

        tool_desciptions = ""
        for tool in tools:
            tool_desciptions += f"{tool.description}\n"
        compiled_prompt = f"""system: 
                You are a friendly assistant that is constantly learning. You speak curtly and have wisdom.
                Answer the following questions as best you can. You have access to the following tools:

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
