# emotion_detection_model.py
from transformers import pipeline

class EmotionDetectionModel:
    def __init__(self):
        self.emotion_detector = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

    def detect_emotion(self, sentence):
        return self.emotion_detector(sentence)
