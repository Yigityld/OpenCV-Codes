import cv2
import numpy as np
cap = cv2.VideoCapture(0)
# cap =cv2.VideoCapture(0) = webcam

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (750, 750))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([18, 94, 140], np.uint8) # hsv range for .........

    upper_yellow = np.array([48, 255, 255], np.uint8)
    # sarı rengi aldık
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # köşeleri çıkardık
    edges = cv2.Canny(mask, 75, 250)
    # ona kenar çizdin
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=100)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    if ret == 0:
        break
        #video bitince çıkarır
    cv2.imshow("mask", frame)
    frame = cv2.flip(frame, 1)
    #cv2.imshow("line", frame)
    #eğer webcamse üste webcam yaz
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
