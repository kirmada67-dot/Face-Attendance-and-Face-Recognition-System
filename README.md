# Face Attendance and Face Recognition System (Prototype)

## Project Overview
This project is a Face Attendance and Face Recognition System developed as an academic prototype using Python. The system uses a webcam to detect and recognize faces in real time through a simple graphical user interface (GUI). An anti-spoofing (liveness detection) mechanism is integrated to reduce proxy attendance using photos or videos. This project focuses on demonstrating the core working concept and is not intended for large-scale or production use.

## Features
- Simple GUI built using Tkinter
- Live webcam feed using OpenCV
- User registration via face image capture
- Face recognition using pre-trained encodings
- Anti-spoofing / liveness detection
- Modular and readable Python codebase

## System Requirements
- Operating System: Linux (recommended)
- Python Version: 3.8 or above
- Hardware: Webcam (built-in or external)

## Mandatory Dependency (Anti-Spoofing)
This project requires the following repository to be cloned inside the project directory (alongside main.py):

https://github.com/minivision-ai/Silent-Face-Anti-Spoofing

This library is used to verify whether the detected face is live or spoofed before recognition.

## Installation & Setup
Clone the project repository:
git clone https://github.com/kirmada67-dot/Face-Attendance-and-Face-Recognition-System.git
cd Face-Attendance-and-Face-Recognition-System

Clone the Silent-Face-Anti-Spoofing repository inside the same folder:
git clone https://github.com/minivision-ai/Silent-Face-Anti-Spoofing.git

(Optional but recommended) Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

Install required Python libraries:
pip install -r requirements.txt
pip install -r Silent-Face-Anti-Spoofing/requirements.txt

Follow the Silent-Face-Anti-Spoofing README to download any required model files.

## Running the Project
python3 main.py

## Project Structure
Face-Attendance-and-Face-Recognition-System/
│
├── main.py
├── util.py
├── dataset/
├── requirements.txt
├── README.md
├── Silent-Face-Anti-Spoofing/

## Libraries Used
- tkinter
- opencv-python
- Pillow
- face_recognition
- NumPy
- Silent-Face-Anti-Spoofing

## Working Flow
1. Webcam captures live video frames.
2. User registers by capturing face images through the GUI.
3. Face encodings are generated from stored images.
4. During login, an anti-spoofing check is performed.
5. If the face is live, face recognition is executed and results are displayed on the GUI.

## Limitations
- Prototype-level implementation
- Accuracy depends on lighting and camera quality
- Not optimized for large datasets
- Not intended for real-world deployment

## Credits
- face_recognition – ageitgey
- Silent-Face-Anti-Spoofing – minivision-ai
- OpenCV & Python community
