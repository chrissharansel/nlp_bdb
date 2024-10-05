import csv
import os

log_file = "logs/therapy_logs.csv"

def log_feedback(user_id, feedback, score):
    if not os.path.exists("logs"):
        os.makedirs("logs")
        
    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_id, feedback, score])
