import cv2
import numpy as np
import face_recognition
import pandas as pd

def load_and_encode_image(image_path):
    """Load an image and get its face encodings."""
    image = cv2.imread(image_path)
    if image is not None:
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(rgb_image)
        return face_encodings
    return []

def load_known_faces(data_csv):
    """Load known faces and their data from a CSV file."""
    known_face_encodings = []
    known_faces_data = pd.read_csv(data_csv)  # Load CSV containing student info and image paths
    
    for index, row in known_faces_data.iterrows():
        image_path = row['Image Path']
        encodings = load_and_encode_image(image_path)
        if encodings:
            known_face_encodings.append(encodings[0])  # Store face encodings

    return known_face_encodings, known_faces_data

def capture_image_from_webcam():
    """Capture an image from the webcam."""
    cap = cv2.VideoCapture(0)
    print("Press 'q' to capture an image.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return frame

def save_attendance_record(record, output_csv):
    """Save the attendance record to a CSV file."""
    df = pd.DataFrame([record])
    df.to_csv(output_csv, mode='a', header=False, index=False)

# File paths
data_csv = 'FulllDb.csv'  # CSV file containing student details (name, age, enrollment, image paths)
attendance_csv = 'attendance.csv'  # CSV file to record attendance

# Load known faces and data
print("Loading known faces and data...")
known_face_encodings, known_data = load_known_faces(data_csv)

# Capture an image from the webcam
print("Capturing image from webcam...")
captured_image = capture_image_from_webcam()
rgb_captured_image = cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)
captured_face_encodings = face_recognition.face_encodings(rgb_captured_image)

# Check for matches
# Check for matches using face distance
if captured_face_encodings:
    print("Comparing faces using face distance...")
    face_distances = face_recognition.face_distance(known_face_encodings, captured_face_encodings[0])
    
    # Find the best match based on the smallest face distance
    best_match_index = np.argmin(face_distances)
      
    if face_distances[best_match_index] < 0.6:  # Adjust tolerance if needed
        print("Match found.")
        # Get matching data from the corresponding row
        student_info = known_data.iloc[best_match_index]
        roll_number = student_info['Roll No']
        name = student_info['Name']
        age = student_info['Age']
        record = {
            'Roll No': roll_number, 
            'Name': name, 
            'Age': age, 
            'Timestamp': pd.Timestamp.now()
        }
        save_attendance_record(record, attendance_csv)
        print(f"Attendance recorded for {name}.")
    else:
        print("No close match found.")
else:
    print("No faces found.")
