# Design
* **Blocks:**  YUI will be made of "blocks" that are connected together to make a graph (at first we will target chains, then DAGs, then cyclic graphs (with limited cycles)). **Each block defines the following:**

   * The inputs it expects including what type they will be.
   * A prompt template
   * How those inputs will be integrated into that prompt template
   * Expected output, including output type and any assertions such as maximum output length, etc.
      * In the future this will probably include an output parser.

* **Prompt registry:** All prompts come from a prompt registry.
   * We enforce that prompt objects should be tied to a specific llm. If we want to use the same type of prompt for another llm, then create a new prompt subclass for that and use it.
      * This will become more important later, when prompt-tuning the optimal prompt is dependent on which llm is the prompt's target.

* For things like chat historys and prompts where different models will need differently formatted strings. The design philosophy, to keep code clean, should be to just create a new subclass that implements the formatting needed for a specific LLM. **DO NOT** make a class which checks the llm type and then switches between a bunch of potential formatting types.
   * This design philosophy might change in the future, but keep it for the first iteration.


# Ideas
* Build LLM agnostic agent application to take notes and answer questions by using RAG on those notes.
* Future work will involve adding more sources of information for RAG and enabling the agent to build and refer to a knowledge graph based on personal notes and past interactions.
* In the future notes that we tell the llm to take should automatically (with user confirmation) be added to existing notes on the same topic.
* Workspace acts as the agent's "scratch pad" feel free to create/retreive documents from there during run time

# Roadmap

\* Don't bother too much with prompt engineering at any step, we will use automatic prompt tuners down the road.

1. ~~Build journal tool for making/reading notes~~
2. Build gpt-3.5 based agent that can use the journal tool
3. Build RAG pipeline to index the journals entries. Use local vector DB.
   * I don't think choice of vector DB matters too much?
4. Build RAG tool to use the vector DB.
5. Give it access to more fun tools
6. Tackle knowledge graph stuff?



------------------
Non-linear tasks

1. Integrate a prompt registry, user should only be allowed to use prompts from the registry. If they want a new prompt, get it from the registry.
   * Implement custom registry or use off the shelf?

* Integrate more tools.

2. Integrate generalizeable output parsers that force expected output from the transformer model. (at the log probs level)

3. (After initial RAG implementation) Implement Colbertv2 based RAG system

4. (Maybe in the future) Generate graphical graph representation of how bocks are connected.




* python version: 3.10.8
* `pip install openai`
* `pip install langchain`
* `pip install google-api-python-client`
* `pip install arxiv`

### Existing Agent frameworks
* Langchain - really good for inspiration, but abstraction hell and too much bloat.
   * Much to take inspiration from, especially the idea behind lang graph
* LLama Index - agent framework focused on RAG integration and QA.
* DSPy - not really an Agent framework, but this is the future of prompt engineering.
   * Truly automatic prompt tuning

### Voice 2 text projects
Faster Whisper, WhisperCPP, and WhisperX seem most promising. Will try using RealtimeSTT first, since it should be a readily packaged accessible version of faster Whisper. Otherwise will try forking it and encorporating faster/accurate sp2txt model.

* https://github.com/KoljaB/RealtimeSTT
   * WebRTCVAD (voice detection)
   * Porcupine (wake word detection)
   * Faster_whisper (sp2txt)
* https://github.com/ggerganov/whisper.cpp
   * Fast cpp whisper
* https://github.com/Picovoice/porcupine
   * Small iot wakeword detector
* https://github.com/openai/whisper
   * The actual whisper
* https://github.com/SYSTRAN/faster-whisper
   * Faster whisper, uses CTranslate2 to speed up transformer architecture
* https://github.com/m-bain/whisperX
   * WhisperX - Faster Whisper under the hood with efficient batch