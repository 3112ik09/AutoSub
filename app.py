from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
import os
from googletrans import Translator
from vosk import Model, KaldiRecognizer
import pyaudio
import json
from googletrans import Translator

app = Flask(__name__, static_folder='autosub/build', static_url_path='')
CORS(app)


@app.route('/voice', methods=['GET'])
@cross_origin()
def speach():
    listen_text = str(request.args['lan'])
    model_loc = '../AutoSub/'+listen_text
    model = Model(model_loc)
    recognizer = KaldiRecognizer(model, 16000)
    cap = pyaudio.PyAudio()
    stream = cap.open(format=pyaudio.paInt16, channels=1,
                      rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
    while True:
        data = stream.read(40960)
        if recognizer.AcceptWaveform(data):
            resp = json.loads(recognizer.Result())
            listen_text = resp["text"]
            return listen_text


@app.route('/api/', methods=['GET'])
@cross_origin()
def data():
    listen_text = str(request.args['query'])
    lan = str(request.args['lan'])
    lan2 = str(request.args['lan2'])
    print(lan)
    print(lan2)
    translator = Translator()
    result = translator.translate(listen_text, src=lan, dest=lan2)
    return result.text


@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    # sec.create_csv()
    app.run()
