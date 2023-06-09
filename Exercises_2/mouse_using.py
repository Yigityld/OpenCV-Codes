import cv2
import numpy as np

cap = cv2.VideoCapture(0)
circles = []
def mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y))

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (500, 440))
    for centers in circles:
        cv2.circle(frame, centers, 2, (255, 0, 0), -1)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("h"):
        circles = []
cap.release()
cv2.destroyAllWindows()