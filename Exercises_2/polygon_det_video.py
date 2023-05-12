import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Settings")
cv2.createTrackbar("Lower_Hue", "Settings", 0, 179, nothing)
cv2.createTrackbar("Lower_Saturation", "Settings", 0, 255, nothing)
cv2.createTrackbar("Lower_Value", "Settings", 0, 255, nothing)
cv2.createTrackbar("Upper_Hue", "Settings", 0, 179, nothing)
cv2.createTrackbar("Upper_Saturation", "Settings", 0, 255, nothing)
cv2.createTrackbar("Upper_Value", "Settings", 0, 255, nothing)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos("Lower_Hue", "Settings")
    ls = cv2.getTrackbarPos("Lower_Saturation", "Settings")
    lv = cv2.getTrackbarPos("Lower_Value", "Settings")
    uh = cv2.getTrackbarPos("Upper_Hue", "Settings")
    us = cv2.getTrackbarPos("Upper_Saturation", "Settings")
    uv = cv2.getTrackbarPos("Upper_Value", "Settings")

    lower_color = np.array([lh, ls, lv])
    upper_color = np.array([uh, us, uv])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        epsilon = 0.02 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        x = approx.ravel()[0]
        y = approx.ravel()[1]
        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
            if len(approx) == 3:
                cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
            elif len(approx) == 4:
                cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
            elif len(approx) > 12:
                cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))
    cv2.imshow("video", mask, )
    cv2.imshow("frame", frame)
    if cv2.waitKey(3) & 0xFF == ord("q"):

        break
cap.release()
cv2.destroyAllWindows()
