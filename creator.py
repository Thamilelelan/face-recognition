import numpy as np
import cv2
import os

# Create a directory for the dataset if it doesn't exist
data_directory = 'dataSet'
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

# Random number to avoid overwriting file names
igniter = 8880
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Change this index if you want to use a different camera
cap = cv2.VideoCapture(0)

# Input ID for the user
id = input('Enter the ID #: ')
sampleNum = 0

while True:
    ret, img = cap.read()
    if not ret:
        print("Failed to capture image. Please check your camera.")
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        sampleNum += 1
        cv2.imwrite(f"{data_directory}/User.{str(id)}.{str(sampleNum * igniter)}.jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.waitKey(100)

    cv2.imshow('frame', img)

    # Exit condition to stop capturing
    if sampleNum >= 210:
        break

cap.release()
cv2.destroyAllWindows()

print('Collection complete!!!')
