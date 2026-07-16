import cv2
from pose.pose_detector import PoseDetector

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Camera failed!")
    exit()

print("Camera opened")

detector = PoseDetector()
import time

time.sleep(2)

while True:

    ret, frame = cap.read()

    print("Frame:", ret)

    if not ret:
        break

    frame, results = detector.detect(frame)

    print("After detect")

    cv2.namedWindow("Pose Test", cv2.WINDOW_NORMAL)
    cv2.imshow("Pose Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()