import json
import os

profile_dir = "user_profiles/"

def save_profile(user_id, profile_data):
    if not os.path.exists(profile_dir):
        os.makedirs(profile_dir)
        
    file_path = os.path.join(profile_dir, f"{user_id}.json")
    with open(file_path, 'w') as f:
        json.dump(profile_data, f)

def load_profile(user_id):
    file_path = os.path.join(profile_dir, f"{user_id}.json")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return None
