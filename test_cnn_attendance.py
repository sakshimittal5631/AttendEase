import cv2
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch
from keras.models import load_model
import pickle


def speak(str1):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.Speak(str1)


model = load_model('face_cnn_model.h5')
with open('data/label_encoder.pkl', 'rb') as f:
    le = pickle.load(f)


video = cv2.VideoCapture(0)


facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')


imgBackground = cv2.imread("background.png")

COL_NAMES = ['NAME', 'TIME']

while True:
    ret, frame = video.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    attendance = None
    date = None
    exist = None

    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50, 50)).reshape(1, 50, 50, 3) / 255.0

        pred = model.predict(resized_img)
        predicted_class = np.argmax(pred)
        name = le.inverse_transform([predicted_class])[0]

        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")
        exist = os.path.isfile("Attendance/Attendance_" + date + ".csv")

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
        cv2.putText(frame, str(name), (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

        attendance = [str(name), str(timestamp)]

    if imgBackground is not None:
        imgBackground[162:162 + 480, 55:55 + 640] = frame
        cv2.imshow("Frame", imgBackground)
    else:
        cv2.imshow("Frame", frame)

    k = cv2.waitKey(1)

    if k == ord('o'):
        speak("Attendance Taken..")
        time.sleep(1)
        filename = "Attendance/Attendance_" + date + ".csv"
        if exist:
            with open(filename, "+a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(attendance)
        else:
            with open(filename, "+a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                writer.writerow(attendance)

    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
