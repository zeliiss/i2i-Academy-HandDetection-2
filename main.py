import cv2

# Kamerayı aç
camera = cv2.VideoCapture(0)

# Kamera açıldı mı kontrol et
if not camera.isOpened():
    print("Kamera açılamadı!")
    exit()

while True:
    # Kameradan görüntü al
    success, frame = camera.read()

    if not success:
        print("Görüntü alınamadı!")
        break

    # Görüntüyü ekranda göster
    cv2.imshow("Hand Detection", frame)

    # Q tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Kamerayı kapat
camera.release()
cv2.destroyAllWindows()