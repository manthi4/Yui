from RealtimeSTT import AudioToTextRecorder as STTRecorder

class Ear():
    def init():
        
    def get_input():
        with STTRecorder(model = 'tiny.en') as recorder:
            return recorder.text()


def main():
    with STTRecorder(model = 'tiny.en') as recorder:
        print(recorder.text())

if __name__ == '__main__':
    main()