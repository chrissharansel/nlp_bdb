import torch
import sys
sys.path.append('e:/BAB/vits')
import os
from tacotron2_model import Tacotron2
from mel_processing import mel_spectrogram_torch

# Ensure the path to your Tacotron2 model is correct
sys.path.append('e:/BAB/vits')

def load_voice_cloning_model():
    model_dir = os.path.join(os.getcwd(), 'models', 'voice_cloning_model')
    model_path = os.path.join(model_dir, 'tacotron2.pth')
    
    if os.path.exists(model_path):
        model = Tacotron2()
        model.load_state_dict(torch.load(model_path, map_location='cpu'))
        model.eval()
        return model
    else:
        raise FileNotFoundError("Voice cloning model not found!")

def clone_voice(text):
    model = load_voice_cloning_model()
    
    # Convert text to mel spectrogram
    mel = mel_spectrogram_torch(text)  # Update function name based on your implementation
    
    # Inference to generate cloned voice
    cloned_voice = model.inference(mel)
    return cloned_voice

# Test data
if __name__ == "__main__":
    test_text = "Hello, this is a test for voice cloning."
    
    try:
        cloned_audio = clone_voice(test_text)
        print("Voice cloning successful!")
        # If needed, you can save the cloned audio to a file here
        # For example:
        write_wav("cloned_voice.wav", cloned_audio, sample_rate)
    except Exception as e:
        print(f"An error occurred: {e}")
