from transformers import pipeline

# Text augmentation pipeline using BERT
augmenter = pipeline('fill-mask', model="bert-base-uncased")

def augment_text(text):
    augmented_text = augmenter(text)[0]["sequence"]
    return augmented_text
