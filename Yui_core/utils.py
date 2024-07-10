import os

from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.fireworks import Fireworks
from llama_index.llms.openai import OpenAI


def get_llm(llm_name="accounts/fireworks/models/mixtral-8x7b-instruct", server="fireworks"):
    """Returns an instantiated instance of whatever llm and serving backend is chosen

    Args:
        llm_name (str, optional): _description_. Defaults to "mixtral-8x7b-instruct".
        server (str, optional): _description_. Defaults to "fireworks".

    Raises:
        ValueError: _description_
        RuntimeError: _description_

    Returns:
        _type_: _description_
    """
    try:
        if server == "fireworks":
            llm = Fireworks(model=llm_name, api_key=os.getenv("FIREWORKS_API_KEY"))
        elif server == "openai":
            llm = OpenAI(temperature=0, model=llm_name)
        else:
            raise ValueError("Unsupported server type")
    except Exception as e:
        raise RuntimeError(f"Error loading {llm_name} from {server}") from e
    return llm


def get_toolkit(tools: list[str]):
    """_summary_

    Args:
        tools (list[str]): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    available_tools: dict[str, list] = {}
    available_tools["Journal_search"] = [print("hello")]

    toolkit = []
    for tool in tools:
        if tool not in available_tools.keys():
            raise ValueError(f"tool {tool} not available")
        toolkit += available_tools[tool]
    return toolkit


def get_agent(llm, toolkit: list, system_prompt: str, verbose=True):
    """_summary_

    Args:
        llm (_type_): _description_
        toolkit (list): _description_
        system_prompt (str): _description_
        verbose (bool, optional): _description_. Defaults to True.

    Returns:
        _type_: _description_
    """
    agent = OpenAIAgent.from_tools(toolkit, llm=llm, verbose=verbose, system_prompt=system_prompt)
    return agent
