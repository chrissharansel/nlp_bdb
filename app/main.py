# main.py
from flask import Flask, render_template, request, jsonify
from models.emotion_detection_model import EmotionDetectionModel
from components.voice_to_text import VoiceToText
from components.text_to_speech import TextToSpeech

app = Flask(__name__)
emotion_model = EmotionDetectionModel()
v2t = VoiceToText()
t2s = TextToSpeech()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotion', methods=['POST'])
def detect_emotion():
    data = request.json
    emotion = emotion_model.detect_emotion(data['text'])
    return jsonify(emotion)

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    audio_file = request.files['audio']
    text = v2t.transcribe_voice(audio_file)
    return jsonify({"text": text})

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text = request.json['text']
    t2s.convert_to_speech(text)
    return jsonify({"status": "Success"})

if __name__ == '__main__':
    app.run(debug=True)
