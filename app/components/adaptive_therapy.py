# adaptive_therapy.py

class AdaptiveTherapy:
    def __init__(self):
        self.exercises = {
            "articulation": "Practice saying 'R' sounds",
            "breathing": "Practice deep breathing"
        }

    def get_exercise(self, therapy_type):
        return self.exercises.get(therapy_type, "Unknown exercise")
