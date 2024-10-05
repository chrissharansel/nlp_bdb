import spacy

# Load the spaCy model by its name
nlp = spacy.load("en_core_web_sm")


# Initialize speech recognizer
recognizer = sr.Recognizer()

def recognize_speech(audio_file):
    """
    Converts speech from an audio file to text using Google Speech API.
    """
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            # Recognizing speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print(f"Recognized Speech: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        return None

def analyze_speech_text(text):
    """
    Uses spaCy to analyze text for speech irregularities and NLP tasks.
    """
    doc = nlp(text)

    # Extract linguistic features (e.g., POS tags, entities) for speech analysis
    for token in doc:
        print(f"Token: {token.text}, POS: {token.pos_}, Dependency: {token.dep_}")

    # Example: Check for sentence length and complexity
    sentences = list(doc.sents)
    print(f"\nTotal Sentences: {len(sentences)}")
    for sent in sentences:
        print(f"Sentence: {sent}, Length: {len(sent)}")

    # Example: Detecting short, incomplete sentences as a proxy for speech irregularity
    for sent in sentences:
        if len(sent) < 5:  # Threshold for short/incomplete sentences
            print(f"Potential Speech Irregularity Detected: {sent}")

def speech_therapy_feedback(text):
    """
    Provides feedback based on the NLP analysis to assist with speech therapy.
    """
    doc = nlp(text)

    # Example: Feedback on using proper sentence structures
    if len(list(doc.sents)) < 2:
        print("Try to form more complete sentences for better communication.")
    else:
        print("Good sentence structure detected!")

    # Example: Identifying repetitive words (common in stuttering)
    words = [token.text for token in doc]
    unique_words = set(words)
    if len(words) - len(unique_words) > 3:  # Threshold for repetition
        print("Repetition of words detected. Try to speak more fluidly.")

# Test with a speech file (in WAV format)
audio_file_path = "wav_arrayMic_FC02S03_0008.wav"  # Replace with your audio file path

# Step 1: Convert speech to text
speech_text = recognize_speech(audio_file_path)

# Step 2: Analyze the text for any irregularities or patterns
if speech_text:
    analyze_speech_text(speech_text)

    # Step 3: Provide feedback for speech therapy
    speech_therapy_feedback(speech_text)
