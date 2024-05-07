# Yui-MHCP001

from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage, AIMessage

# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from langchain_openai import ChatOpenAI
from RealtimeSTT import AudioToTextRecorder as STTRecorder
from Yui_perf.prompts import YuiPrompts
from tools.basic_tools import multiply
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
import os


with open("openai.key", "r") as file:
    Oai_key = file.read().strip()


class YuiAgent:

    def __init__(self, tools, prompt=YuiPrompts.react_agent, llm=None, limit=100):
        self.prompt = prompt
        self.chat_history = ChatMessageHistory()
        self.llm = llm
        self.limit = limit

        if self.llm is None:
            self.llm = ChatOpenAI(
                model="gpt-3.5-turbo",
                temperature=0,
                api_key=os.environ["Oai_key"],
                max_tokens=45,
            )

        # creat_tool_calling_agent creates an agent that expects/uses a placeholder in the prompt for agent_scratchpad
        self._agent = create_tool_calling_agent(llm, tools, prompt)
        self._executor = AgentExecutor(agent=self._agent, tools=tools, verbose=True)

    def check_ticker(self):
        if self.limit <= 0:
            print("agent limit reachd, bye. < end convo >")
            exit()
        self.limit -= 1

    def add_user_input(self, user_input: str):
        if self.is_bye(user_input):
            print("bye! <ending conversation>")
            exit()
        self.chat_history.add_user_message(user_input)

    def get_response(self) -> str:
        self.check_ticker()
        response_raw = self._executor.invoke(
            {"chat_history": self.chat_history.messages}
        )
        response_msg = AIMessage(content=response_raw["output"])
        self.chat_history.add_ai_message(response_msg)
        return response_msg.content

    def is_bye(i: str) -> bool:
        i = i.lower()
        return (
            (i == "bye")
            | (i == "goodbye")
            | (i == "good bye")
            | (i == "bye.")
            | (i == "goodbye.")
            | (i == "good bye.")
        )


def main_agent_loop(prompt, llm):
    prompt = YuiPrompts.react_agent
    chain = get_chain(prompt)
    history = ChatMessageHistory()

    with STTRecorder(model="tiny.en") as recorder:
        while True:
            i = recorder.text()
            # i = input("speak >> ")
            print("speak >> ", i)
            if is_bye(i):
                exit()
            history.add_user_message(i)
            res = chain.invoke({"chat_history": history.messages})
            history.add_ai_message(res)
            print(f"Ai >> {res.content}")


def main():
    print(type(multiply))
    tools = [multiply]
    yui = YuiAgent(tools=tools, limit=10)

    while True:
        i = input("Usr In >> ")
        yui.add_user_input(i)
        resp = yui.get_response()
        print(f"Ai >> {resp}")


if __name__ == "__main__":
    with open("openai.key", "r") as file:
        Oai_key = file.read().strip()
        os.environ["Oai_key"] = Oai_key
    main()
