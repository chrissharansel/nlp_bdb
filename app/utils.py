# utils.py
import os

def save_audio_file(file, path):
    filename = os.path.join(path, file.filename)
    file.save(filename)
    return filename
