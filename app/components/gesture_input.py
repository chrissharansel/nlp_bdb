# gesture_input.py
import cv2
import numpy as np

class GestureInput:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.hand_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_hand.xml')  # Use a pre-trained hand cascade

    def track_gesture(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            hands = self.hand_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cv2.imshow('Gesture Recognition', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    gesture_input = GestureInput()
    gesture_input.track_gesture()
