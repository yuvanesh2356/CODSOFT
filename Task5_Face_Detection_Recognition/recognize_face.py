import cv2

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

cap = cv2.VideoCapture(0)

print("Face Recognition Started...")
print("Press Q to exit")

while True:
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]

        id, confidence = recognizer.predict(face)

        if confidence < 80:
            name = "Yuvanesh"
        else:
            name = "Unknown"

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (255, 0, 0),
            2
        )
        (text_width, text_height), _ = cv2.getTextSize(
            name,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            2
        )  

        text_x = x + (w // 2) - (text_width // 2)
        text_y = y - 10

        cv2.putText(
            frame,
            name,
            (text_x, text_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )


    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
