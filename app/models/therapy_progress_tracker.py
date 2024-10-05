# therapy_progress_tracker.py

class TherapyProgressTracker:
    def __init__(self):
        self.progress = {}

    def update_progress(self, user_id, exercise, score):
        if user_id not in self.progress:
            self.progress[user_id] = []
        self.progress[user_id].append({'exercise': exercise, 'score': score})

    def get_progress(self, user_id):
        return self.progress.get(user_id, [])
