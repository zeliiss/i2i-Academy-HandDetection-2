import cv2
import mediapipe as mp
import urllib.request
import os


model_path = "hand_landmarker.task"
if not os.path.exists(model_path):
    print("Gerekli model dosyası indiriliyor, lütfen terminali kapatma...")
    url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
    urllib.request.urlretrieve(url, model_path)


options = mp.tasks.vision.HandLandmarkerOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path=model_path),
    running_mode=mp.tasks.vision.RunningMode.IMAGE,
    num_hands=1
)
landmarker = mp.tasks.vision.HandLandmarker.create_from_options(options)


camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Kamera açılamadı!")
    exit()


tip_ids = [4, 8, 12, 16, 20]

while True:
    success, frame = camera.read()
    if not success:
        break

   
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    
    
    result = landmarker.detect(mp_image)
 
    if result.hand_landmarks:
        for hand_landmarks in result.hand_landmarks:
            
            
            h, w, c = frame.shape
            for landmark in hand_landmarks:
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(frame, (cx, cy), 6, (255, 0, 255), cv2.FILLED)

            
            fingers = []

            if hand_landmarks[tip_ids[0]].x < hand_landmarks[tip_ids[0] - 1].x:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1, 5):
                if hand_landmarks[tip_ids[id]].y < hand_landmarks[tip_ids[id] - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total_fingers = fingers.count(1)

            
            cv2.putText(frame, f"Acik Parmak: {total_fingers}", (50, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Hand Detection", frame)

    # Q tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()