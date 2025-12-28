# Face Attendance and Face Recognition System (Prototype)

## Project Overview
This project is a **Face Attendance and Face Recognition System** developed as an academic prototype using Python.  
The system uses a webcam to detect and recognize faces in real time through a simple graphical user interface (GUI).  
An **anti-spoofing (liveness detection)** mechanism is also integrated to reduce proxy attendance using photos or videos.

This project focuses on demonstrating the **core working concept** and is not intended for large-scale or production use.

---

## Features
- Simple GUI built using **Tkinter**
- Live webcam feed using **OpenCV**
- User registration via face image capture
- Face recognition using pre-trained encodings
- Anti-spoofing / liveness detection
- Modular Python codebase

---

## System Requirements
- **OS:** Linux (recommended)
- **Python:** 3.8+
- **Hardware:** Webcam (built-in or external)

---

## Mandatory Dependency (Anti-Spoofing)
This project **requires** the following repository to be cloned inside the project directory:

https://github.com/minivision-ai/Silent-Face-Anti-Spoofing

yaml
Copy code

This library is used to verify whether the detected face is **live or spoofed**.

---

## Installation & Setup

### Step 1: Clone this repository
git clone https://github.com/kirmada67-dot/Face-Attendance-and-Face-Recognition-System.git
cd Face-Attendance-and-Face-Recognition-System
Step 2: Clone Silent-Face-Anti-Spoofing repository
bash
Copy code
git clone https://github.com/minivision-ai/Silent-Face-Anti-Spoofing.git
Step 3: (Optional) Create virtual environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate
Step 4: Install required libraries
bash
Copy code
pip install -r requirements.txt
pip install -r Silent-Face-Anti-Spoofing/requirements.txt
Follow the Silent-Face-Anti-Spoofing README for required model files.

Running the Project
bash
Copy code
python3 main.py
Project Structure
css
Copy code
Face-Attendance-and-Face-Recognition-System/
│
├── main.py
├── util.py
├── dataset/
├── requirements.txt
├── README.md
├── Silent-Face-Anti-Spoofing/
Libraries Used
tkinter

opencv-python

Pillow

face_recognition

NumPy

Silent-Face-Anti-Spoofing

Working Flow
Webcam captures live video.

User registers by capturing face images.

Face encodings are generated.

During login:

Anti-spoofing check is performed

Face recognition is executed

Result is displayed on the GUI.

Limitations
Prototype-level system

Accuracy depends on lighting and camera quality

Not designed for large-scale deployment

Credits
face_recognition – ageitgey

Silent-Face-Anti-Spoofing – minivision-ai

OpenCV & Python community
