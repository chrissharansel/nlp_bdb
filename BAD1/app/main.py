from flask import Flask, request, jsonify
from app.user_profiles import save_profile, load_profile
from app.feedback import log_feedback
from app.emotion_recognition import predict_emotion
from app.voice_cloning import clone_voice
from app.gpt_predictor import predict_context
from app.bert_augmenter import augment_text

app = Flask(__name__)

@app.route('/save-profile', methods=['POST'])
def save_user_profile():
    data = request.json
    user_id = data.get("user_id")
    profile_data = data.get("profile_data")
    save_profile(user_id, profile_data)
    return jsonify({"message": "Profile saved successfully."})

@app.route('/feedback', methods=['POST'])
def log_user_feedback():
    data = request.json
    user_id = data.get("user_id")
    feedback = data.get("feedback")
    score = data.get("score")
    log_feedback(user_id, feedback, score)
    return jsonify({"message": "Feedback logged successfully."})

@app.route('/emotion-recognition', methods=['POST'])
def recognize_emotion():
    data = request.json
    text = data.get("text")
    emotion = predict_emotion(text)
    return jsonify({"emotion": emotion})

@app.route('/voice-cloning', methods=['POST'])
def clone_user_voice():
    data = request.json
    user_id = data.get("user_id")
    audio_data = data.get("audio_data")  # Assuming base64 audio data
    cloned_audio = clone_voice(user_id, audio_data)
    return jsonify({"message": "Voice cloned successfully."})

@app.route('/gpt-predict', methods=['POST'])
def gpt_prediction():
    data = request.json
    text = data.get("text")
    prediction = predict_context(text)
    return jsonify({"predicted_text": prediction})

@app.route('/bert-augment', methods=['POST'])
def bert_augment_text():
    data = request.json
    text = data.get("text")
    augmented_text = augment_text(text)
    return jsonify({"augmented_text": augmented_text})

if __name__ == '__main__':
    app.run(debug=True)
