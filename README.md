# Face Recognition

This project is a simple face recognition system built using OpenCV in Python. It allows you to collect face images, train a recognition model, and identify users based on assigned IDs and names.

## Features

- Data Collection: Captures face images and assigns unique IDs.
- Training: Trains an LBPH (Local Binary Patterns Histograms) model on the collected face images.
- Face Recognition: Recognizes faces from live video feed and displays the name and confidence level of the recognized users.

## Installation

1. Clone the repository :
   
   ```bash
   git clone https://github.com/Thamilelelan/face-recognition.git
   cd face-recognition

2. Install dependencies :

   ```bash
   pip install opencv-python opencv-python-headless numpy pillow

3. Create two folders under the same directory named `dataSet` and `trainer`

## How to run 

1. Run `creator.py` to create a dataSet of the user's face in `dataSet`. Remember the id to input for the user
2. Run `trainer.yml` to train the model on the dataset of images. The trainer model will be stored under the `trainer` folder you created as `trainer.yml`
3. Run `detector.py` to start detecting the faces. You can set the names of the users to the correct id that you gave while running `creator.py`

## Dependencies

- Python 3.x
- OpenCV (opencv-python)
- NumPy
- Pillow (PIL)
