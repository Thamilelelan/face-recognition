'''import cv2
import os

# Path to the trained model
trainer_path = os.path.join(os.path.dirname(__file__), 'trainer', 'trainer.yml')
# Initialize face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained model file
try:
    recognizer.read(trainer_path)
    print("[INFO] Model loaded successfully.")
except cv2.error as e:
    print(f"[ERROR] Could not load model. Make sure 'trainer.yml' exists in the 'trainer' folder.\nDetails: {e}")
    exit()

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to capture frame. Please check your camera.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Get the ID and confidence from the recognizer
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # Check confidence level
        if confidence < 50:
            # Message for recognized user
            text = f"User {id} recognized - {round(100 - confidence, 2)}% confidence"
            color = (0, 255, 0)  # Green for recognized face
        else:
            text = "Unknown user"
            color = (0, 0, 255)  # Red for unrecognized face

        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        # Display recognition text
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Show video feed
    cv2.imshow('Face Recognition', frame)

    # Break the loop with 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
'''

import cv2
import os

# Path to the trained model
trainer_path = os.path.join(os.path.dirname(__file__), 'trainer', 'trainer.yml')
# Initialize face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained model file
try:
    recognizer.read(trainer_path)
    print("[INFO] Model loaded successfully.")
except cv2.error as e:
    print(f"[ERROR] Could not load model. Make sure 'trainer.yml' exists in the 'trainer' folder.\nDetails: {e}")
    exit()

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize an empty dictionary to hold ID to name mapping
id_to_name = {}

# Number of users to be recognized
num_users = int(input("Enter the number of users: "))

# Prompt for user names
for i in range(1, num_users + 1):
    name = input(f"Enter the name for ID {i}: ")
    id_to_name[i] = name

# Start video capture
cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to capture frame. Please check your camera.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Get the ID and confidence from the recognizer
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # Check confidence level
        if confidence < 50:
            # Retrieve name from the ID
            name = id_to_name.get(id, "Unknown User")  # Default to "Unknown User" if ID not found
            text = f"{name} - {round(100 - confidence, 2)}% confidence"
            color = (0, 255, 0)  # Green for recognized face
        else:
            text = "Unknown user"
            color = (0, 0, 255)  # Red for unrecognized face

        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        # Display recognition text
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Show video feed
    cv2.imshow('Face Recognition', frame)

    # Break the loop with 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
