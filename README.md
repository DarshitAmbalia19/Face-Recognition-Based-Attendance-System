# Face Recognition-Based Attendance System

This project is a Python-based face recognition attendance system that uses OpenCV, face_recognition, and pandas libraries to identify individuals and log attendance. The system is designed to work with a webcam to capture real-time images and match them against a preloaded database of known faces stored in a CSV file.

## Features

- Real-time face recognition using a webcam.
- Automatic matching of captured faces with a known database.
- Logging attendance records into a CSV file with timestamp details.
- Easy integration with new databases by simply updating the CSV file.

## Project Files

1. **attendence_system.py**: The main script containing the logic for face recognition and attendance recording.
2. **FulllDb.csv**: A database of known individuals with their details (Name, Roll No, Age, Image Path).
3. **attendance.csv**: The output file where attendance records are stored, including timestamp information.

## Requirements

To run this project, you need:

- Python 3.7 or higher
- Required libraries:
  - OpenCV
  - face_recognition
  - pandas
  - numpy

Install the dependencies using pip:

```bash
pip install opencv-python face_recognition pandas numpy
```

## usage

- Prepare the Database:
      Populate FulllDb.csv with the details of individuals (Name, Roll No, Age) and the paths to their images.
- Run the Program:
      Execute the Python script:
      ```bash
      python attendence_system.py
      ```
      The script will load the known faces and launch the webcam.

- Capture and Compare:
      Press q to capture an image using the webcam.
      The system will compare the captured image against the database and log the attendance if a match is found.

- Attendance Records:
      If a match is found, the individual's details and timestamp are logged in attendance.csv.


## how it works

- Load and Encode:
      Known faces are loaded from the images specified in the FulllDb.csv file and encoded using face_recognition.
- Real-Time Capture:
      The system uses a webcam to capture a real-time image and encodes the detected face(s).
- Face Comparison:
      The captured face encodings are compared with known encodings using a face distance metric to find the best match.

- Attendance Logging:
      If a match is found, the individual's details and timestamp are logged in attendance.csv.


## Developer

- [Darshit Ambalia](https://github.com/DarshitAmbalia19)

