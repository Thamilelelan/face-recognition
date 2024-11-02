import os
import numpy as np
from PIL import Image
import cv2
import time

# Initialize the recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Path to the dataSet directory within the face-recog folder
dataset_path = os.path.join(os.path.dirname(__file__), 'dataSet')

def getImagesAndLabels(path):
    # Check if path exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"The path does not exist: {path}")

    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    Ids = []

    for imagePath in imagePaths:
        if(os.path.split(imagePath)[-1].split(".")[-1] != 'jpg'):
            continue

        pilImage = Image.open(imagePath).convert('L')
        print(imagePath)
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])

        faces = detector.detectMultiScale(imageNp)
        print('Extracting Face...')
        for (x, y, w, h) in faces:
            print('Adding cropped image to face sample archive')
            faceSamples.append(imageNp[y:y+h, x:x+w])
            Ids.append(Id)
    return faceSamples, Ids

# Ensure the dataset path is correct
try:
    faces, Ids = getImagesAndLabels(dataset_path)
    print('[+] Analysis in progress...')
    recognizer.train(faces, np.array(Ids))
    recognizer.save('trainer/trainer.yml')
    print('[!!!] Image Analysis Complete!')
    time.sleep(2)
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")
