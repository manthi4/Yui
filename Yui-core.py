# Yui-MHCP001

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from langchain_openai import ChatOpenAI
from RealtimeSTT import AudioToTextRecorder as STTRecorder
from RealtimeTTS import TextToAudioStream, SystemEngine, CoquiEngine



with open("openai.key", "r") as file:
    Oai_key = file.read().strip()


def get_chain():
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant. Answer all questions to the best of your ability. You speak directly and get to the point. You are witty and playful but also reliable and profound. You are a monk. Your name is Zenith",
            ),
            MessagesPlaceholder(variable_name="chat_history"),
        ]
    )

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=Oai_key, max_tokens=45)
    chain = prompt | llm
    return chain

def is_bye( i : str ) -> bool:
    i = i.lower()
    return (i == "bye") | (i == "goodbye") | (i == "good bye") | (i == "bye.") | (i == "goodbye.") | (i == "good bye.")

def main():
    chain = get_chain()
    history = ChatMessageHistory()
    engine = CoquiEngine() # replace with your TTS engine
    stream = TextToAudioStream(engine)

    with STTRecorder(model = 'tiny.en') as recorder:
        while True:
            i = recorder.text()
            # i = input("speak >> ")
            print("speak >> ", i)
            if is_bye(i):
                exit()
            history.add_user_message(i)
            res = chain.invoke({"chat_history":history.messages})
            history.add_ai_message(res)
            print(f"Ai >> {res.content}")
            stream.feed(res.content)
            stream.play()


if __name__ == '__main__':
    main()
