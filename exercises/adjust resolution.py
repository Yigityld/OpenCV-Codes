import cv2
import numpy as np

Window_name = "CapVideo"
cv2.namedWindow(Window_name)
cap = cv2.VideoCapture(0)

print("Width:"+ str(cap.get(3)), "Height"+ str(cap.get(4)))

cap.set(3, 1280)
cap.set(4, 720)
print("Width:"+ str(cap.get(3)), "Height"+ str(cap.get(4)))

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow(Window_name, frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()