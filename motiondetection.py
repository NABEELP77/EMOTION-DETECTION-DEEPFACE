import cv2
from deepface import DeepFace

# Initialize webcam capture
cap = cv2.VideoCapture(0)

while True:

    #Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Use DeepFace to analyze the frame for emotions
    try:
        # The DeepFace.analyze method takes care of face detection and emotion recognition
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        # Extract emotion with the highest probability
        dominant_emotion = analysis[0]['dominant_emotion']

        # Display the detected emotion on the frame
        cv2.putText(frame, f"Emotion: {dominant_emotion}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    except Exception as e:
        print("Face not detected or error:", e)

    # Show the frame with emotion
    cv2.imshow("Emotion Detection", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the windows
cap.release()
cv2.destroyAllWindows()