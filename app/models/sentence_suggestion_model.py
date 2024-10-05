# sentence_suggestion_model.py
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class SentenceSuggestionModel:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')

    def suggest_next(self, input_text):
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt')
        output_ids = self.model.generate(input_ids, max_length=50, num_return_sequences=1)
        return self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
