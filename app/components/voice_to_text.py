# voice_to_text.py
import speech_recognition as sr

class VoiceToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe_voice(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            audio = self.recognizer.listen(source)
            text = self.recognizer.recognize_google(audio)
            return text
