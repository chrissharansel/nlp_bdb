import cv2
import pyttsx3  # For text-to-speech conversion
import numpy as np

class EyeGazeAAC:
    def __init__(self):
        # Load the pre-trained Haar cascades for face and eye detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        self.cap = cv2.VideoCapture(0)
        
        # Text-to-speech engine initialization
        self.tts_engine = pyttsx3.init()
        self.words_grid = ["Hello", "Yes", "No", "Help", "Please", "Thank you"]
        self.grid_size = len(self.words_grid)
    
    def display_grid(self, frame):
        """
        Display the communication grid with words on the frame.
        """
        h, w, _ = frame.shape
        grid_width = w // self.grid_size

        for i in range(self.grid_size):
            cv2.rectangle(frame, (i * grid_width, h - 100), ((i + 1) * grid_width, h), (0, 255, 0), 2)
            cv2.putText(frame, self.words_grid[i], ((i * grid_width) + 20, h - 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    def detect_eye_focus(self, x, w, gaze_x):
        """
        Detect which word the user is focusing on based on gaze location.
        """
        relative_x = gaze_x - x  # Eye gaze position relative to the face
        grid_section_width = w // self.grid_size
        
        if relative_x > 0:
            focused_word_index = int(relative_x // grid_section_width)
            if 0 <= focused_word_index < self.grid_size:
                return self.words_grid[focused_word_index]
        return None
    
    def track_eye_movement(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)  # Detect faces

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                eyes = self.eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    # Draw rectangles around eyes
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

                    # Here we estimate that the user’s gaze is aligned with the x-coordinate of the eyes
                    focused_word = self.detect_eye_focus(x, w, ex + (ew // 2))
                    if focused_word:
                        cv2.putText(frame, f'Selected: {focused_word}', (50, 50), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                        # Convert text to speech if the word is selected for a while
                        self.tts_engine.say(focused_word)
                        self.tts_engine.runAndWait()

            # Display the grid of words
            self.display_grid(frame)

            # Show the result frame
            cv2.imshow('Eye Gaze AAC System', frame)

            # Break loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release resources
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    aac_system = EyeGazeAAC()
    aac_system.track_eye_movement()
