import cv2

from pose.pose_detector import PoseDetector


cap = cv2.VideoCapture(0)

detector = PoseDetector()

while True:

    success, frame = cap.read()

    if not success:
        break

    frame, results = detector.detect(frame)

    cv2.imshow("AI Fitness Trainer", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()