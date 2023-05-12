import cv2
import numpy as np

cap = cv2.VideoCapture(0)
_, first_frame = cap.read()
first_frame = cv2.resize(first_frame, (640, 640))
gray_first = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(gray_first, (5, 5), 0)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 640))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    frame = cv2.flip(frame, 1)
    # karşılaştırma yapar.
    diff = cv2.absdiff(first_gray, gray)
    # grilerden kurtulmak için
    _, diff = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)
    cv2.imshow("frame", frame)
    cv2.imshow("first_frame", first_frame)
    cv2.imshow("diff", diff)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
