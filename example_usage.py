import os

with open("openai.key", "r") as file:
    Oai_key = file.read().strip()

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
