## Fireworks.ai
* Used for the grammar capability:
   * https://readme.fireworks.ai/docs/structured-output-grammar-based

## LangFuse
* Used for prompt registry and tracing
* https://langfuse.com/docs/deployment/local

## Deps
* python version: 3.10.8
* dependencies in requirements.in
   * Use uv (https://github.com/astral-sh/uv)
   ~~~
      uv pip compile requirements.in -o requirements.txt
      uv pip sync requirements.txt
   ~~~
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
