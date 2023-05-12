import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# hazır fonk (birinci ışığı ayarlar daha fazla beyaz çizer gibi ,ikinci cisimlerin görünmesini ayarlar, üçüncü gölge
substractor = cv2.createBackgroundSubtractorMOG2(100, 50, True)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 640))
    mask = substractor.apply(frame)
    cv2.imshow("mask", mask)
    cv2.imshow("oriji", frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()