from vosk import Model, KaldiRecognizer
import pyaudio
import json
from googletrans import Translator
model = Model('/home/ishu/Desktop/AutoSub/hi')

recognizer = KaldiRecognizer(model, 16000)

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1,
                  rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        resp = json.loads(recognizer.Result())
        listen_text = resp["text"]
        print(listen_text)
        # translator = Translator()
        # if listen_text != "":
        #     result = translator.translate(listen_text, src='hi', dest='en')
        #     print(result.text)
