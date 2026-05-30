import cv2
import os
import numpy as np

# Create recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

dataset_path = "dataset"

faces = []
ids = []

for image_name in os.listdir(dataset_path):

    image_path = os.path.join(dataset_path, image_name)

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    faces.append(img)

    ids.append(1)  # Your face ID

ids = np.array(ids)

# Train model
print("Training model...")

recognizer.train(faces, ids)

# Save trained model
recognizer.save("trainer.yml")

print("Training completed successfully!")
print("Model saved as trainer.yml")
