import cv2
import os

if not os.path.exists("dataset"):
    os.makedirs("dataset")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

count = 0

print("Face Capture Started...")
print("Look at the camera")
print("Press Q to stop")

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

        count += 1

        face = gray[y:y+h, x:x+w]

        cv2.imwrite(f"dataset/user_{count}.jpg", face)

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            f"Images Captured: {count}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Face Capture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
        break

cap.release()
cv2.destroyAllWindows()

print(f"{count} face images saved successfully!")
