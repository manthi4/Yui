# Yui-MHCP001

from langchain.llms import OpenAI
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.agents import initialize_agent, AgentType, AgentExecutor, load_tools
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from tools.helper import Helper
from tools.journal import Journal

class Yui:

    def __init__(self):
        llm  = OpenAI(temperature = 0)
        chat_llm = ChatOpenAI(temperature = 0)

        search = GoogleSearchAPIWrapper(k = 5) # searches top 10 results by default
        google_search_tool = Tool(
            name = "Google Search",
            description = "Search Google for recent results. Can be useful for finding information.",
            func = search.run
        )

        _helper = Helper()
        mini_helper = Tool(
            name = "Helper", 
            description = "Helper is a large language model that can help do simple creative tasks such as writing stories, poems, and having conversations. As input you must give helper a detailed prompt with context. ",
            func = _helper.run
        )

        _juornal = Journal()
        journal_writer = Tool(
            name = "Journal Writer", 
            description = "This tool can add to today's journal entry. Input should have context",
            func = _juornal.write
        )
        journal_reader = Tool(
            name = "Journal Reader", 
            description = "This tool can be used to read information from journal entry of a specified date. Input to this tool should be in the format yyyy-mm-dd",
            func = _juornal.get
        )

        more_tools = load_tools(["arxiv"])

        Major_toolkit = [google_search_tool, mini_helper, journal_writer, journal_reader] + more_tools



        self.Yui_0 = initialize_agent(Major_toolkit, llm, agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True) #returns an agent executor
        # Yui_0 = initialize_agent(Major_toolkit, llm, agent = AgentType.SELF_ASK_WITH_SEARCH, verbose = True) #returns an agent executor
    def run(self, prompt):
        self.Yui_0.run(prompt)
# Yui_0.run("Hi, find a pasta recipe. Then write a poem about it's ingredients.")