# __init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    from app.models import emotion_detection_model, sentence_suggestion_model, real_time_speech_model
    from app.components import voice_to_text, text_to_speech, adaptive_therapy

    return app
