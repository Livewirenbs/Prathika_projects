import cv2
from deepface import DeepFace

# Open Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    try:
        # Analyze Face (Only Age + Emotion)
        result = DeepFace.analyze(
            frame,
            actions=['age', 'emotion'],
            enforce_detection=False
        )

        # Get Data
        age = result[0]['age']
        emotion = result[0]['dominant_emotion']

        # Display Text
        text = f"Age: {age} | Emotion: {emotion}"

        # Show Prediction
        cv2.putText(
            frame,
            text,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    except Exception as e:
        print("Error:", e)

    # Show Webcam
    cv2.imshow("AI Human Analyzer", frame)

    # Press q to Quit
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

# Release Camera
cap.release()
cv2.destroyAllWindows()