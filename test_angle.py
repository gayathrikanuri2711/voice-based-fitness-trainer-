import cv2
import mediapipe as mp

from pose.pose_detector import PoseDetector
from pose.angle import calculate_angle



# Open webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("❌ ERROR: Camera could not be opened.")
    exit()


# Initialize pose detector
detector = PoseDetector()




while True:

    success, frame = cap.read()

    
    if not success:
        
        break

    # Detect pose
    frame, results = detector.detect(frame)

    if results.pose_landmarks:

       

        landmarks = results.pose_landmarks.landmark

        shoulder = (
            landmarks[
                mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value
            ].x,
            landmarks[
                mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value
            ].y
        )

        elbow = (
            landmarks[
                mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value
            ].x,
            landmarks[
                mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value
            ].y
        )

        wrist = (
            landmarks[
                mp.solutions.pose.PoseLandmark.LEFT_WRIST.value
            ].x,
            landmarks[
                mp.solutions.pose.PoseLandmark.LEFT_WRIST.value
            ].y
        )

        angle = calculate_angle(
            shoulder,
            elbow,
            wrist
        )

        
        cv2.putText(
            frame,
            f"Elbow Angle: {int(angle)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    else:
        print("❌ No pose detected")

    cv2.imshow("Angle Detection", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        
        break

cap.release()
cv2.destroyAllWindows()

