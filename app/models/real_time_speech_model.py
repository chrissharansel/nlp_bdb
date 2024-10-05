# real_time_speech_model.py
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

class RealTimeSpeechModel:
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained('t5-small')
        self.model = T5ForConditionalGeneration.from_pretrained('t5-small')

    def reconstruct_sentence(self, partial_sentence):
        input_text = f"complete: {partial_sentence}"
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt')
        output_ids = self.model.generate(input_ids, max_length=50)
        return self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
