import cv2
import numpy as np
import time

capture = cv2.VideoCapture("test_video1.mp4")

while True:
    capture.set(cv2.CAP_PROP_FPS, 12)
    _, frame = capture.read()
    cv2.imshow("frame", frame)
    key = cv2.waitKey(500)
    if key == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()