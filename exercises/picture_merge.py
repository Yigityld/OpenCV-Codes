import cv2
import numpy as np


def nothing(x):
    pass

img1 = cv2.imread("aircraft.jpg")
img1 = cv2.resize(img1, (640, 480))
img2 = cv2.imread("balls.jpg")
img2 = cv2.resize(img2, (640, 480))

output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)


cv2.namedWindow("Transition app")

cv2.createTrackbar("Alpha Beta", "Transition app", 0, 1000, nothing)

while True:
    cv2.imshow("Transition app", output)
    Alpha = cv2.getTrackbarPos("Alpha Beta", "Transition app")/1000

    Beta = 1 - Alpha
    output = cv2.addWeighted(img1 , Alpha, img2, Beta, 0)
    print(Alpha, Beta)

    if cv2.waitKey(1) == 27:
        break


cv2.waitKey(0)
cv2.destroyAllWindows()