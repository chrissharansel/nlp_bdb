import transformers

# Load GPT-2 model
model_name = "gpt2"
tokenizer = transformers.GPT2Tokenizer.from_pretrained(model_name)
model = transformers.GPT2LMHeadModel.from_pretrained(model_name)

def predict_context(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_length=50)
    predicted_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return predicted_text
