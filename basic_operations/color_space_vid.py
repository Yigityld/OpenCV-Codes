import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret == 0:
        break
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
    frame = cv2.flip(frame, 1)
    cv2.imshow("Video", frame)

cap.release()
cv2.destroyAllWindows()