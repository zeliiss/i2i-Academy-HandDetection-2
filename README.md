# Hand Detection and Finger Counting

This project is a real-time finger counting application developed using OpenCV and MediaPipe to learn the basics of computer vision.

## Project  Steps
This project successfully implements the 4 required steps:
1. **Open Camera:** Captures real-time video using `cv2.VideoCapture(0)`.
2. **Hand and Landmark Detection:** Detects and draws 21 hand landmarks using the MediaPipe Tasks API.
3. **Logical Calculation:** Calculates whether fingers are open or closed (X-axis logic for the thumb, Y-axis logic for the other four fingers).
4. **Display Text:** Displays the total count of open fingers on the live video feed using `cv2.putText`.

## How to Run

Install the required libraries:
```bash
pip install opencv-python mediapipe
