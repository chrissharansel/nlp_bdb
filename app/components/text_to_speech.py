# text_to_speech.py
from gtts import gTTS
import os

class TextToSpeech:
    def __init__(self, language='en'):
        self.language = language

    def convert_to_speech(self, text, output_file="output.mp3"):
        tts = gTTS(text=text, lang=self.language)
        tts.save(output_file)
        os.system(f"mpg321 {output_file}")
