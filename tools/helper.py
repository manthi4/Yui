from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


class Helper:
    def __init__(self):
        self.llm  = OpenAI(temperature = 0)
        self.base_prompt = "You are a helpful assistant. You answer requests truthfully and with tact."
        self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.base_prompt)
        self.human_message_prompt = HumanMessagePromptTemplate(
            prompt = PromptTemplate( input_variables = ["text"], template = "{text}")
            )
        self.chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt, self.human_message_prompt])
        self.helper_chain = LLMChain(llm = self.llm, prompt = self.chat_prompt)
    def run(self, prompt):
        return self.helper_chain.run(prompt)
