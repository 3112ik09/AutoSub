from vosk import Model, KaldiRecognizer
import pyaudio
import json
from googletrans import Translator
import moviepy.editor as mp
import wave
import struct
import time
import sys
model = Model('/home/ishu/Desktop/AutoSub/ja')

# length of data to read.
chunk = 4096

# convert audio..
clip = mp.VideoFileClip(r"/home/ishu/Desktop/AutoSub/vid2.mp4")
clip.audio.write_audiofile(r"con.wav")

wf = wave.open(r'/home/ishu/Desktop/AutoSub/con.wav', 'rb')

rec = KaldiRecognizer(model, wf.getframerate())
transcription = []
while True:
    data = wf.readframes(100000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        # Convert json output to dict
        result_dict = json.loads(rec.Result())
        # print(result_dict)
        # Extract text values and append them to transcription list
        transcription.append(result_dict.get("text", ""))

        listen_text = result_dict.get("text", "")
        # print(listen_text)
        translator = Translator()
        if listen_text != "":
            result = translator.translate(listen_text, src='ja', dest='en')
            # print(result.src)
            # print(result.dest)
            print(result.text)

# Get final bits of audio and flush the pipeline
final_result = json.loads(rec.FinalResult())
transcription.append(final_result.get("text", ""))

# merge or join all list elements to one big string
transcription_text = ' '.join(transcription)
print(transcription_text)
