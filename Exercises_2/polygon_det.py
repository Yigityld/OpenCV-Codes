import cv2
import numpy as np
# kontur yaoıcaksın kenarlara göre ilerliceksin

font = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.FONT_HERSHEY_COMPLEX
img1 = cv2.imread("polygons.png")
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    cv2.drawContours(img1, [approx], 0, (0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        cv2.putText(img1, "Triangle", (x, y), font, 1, (0, 0, 0))
    elif len(approx) == 4:
        cv2.putText(img1, "Rectangle", (x, y), font, 1, (0, 0, 0))
    elif len(approx) == 5:
        cv2.putText(img1, "Pentagon", (x, y), font, 1, (0, 0, 0))
    elif len(approx) == 6:
        cv2.putText(img1, "Hexagon", (x, y), font, 1, (0, 0, 0))
    else:
        cv2.putText(img1, "Ellipse", (x, y), font, 1, (0, 0, 0))
cv2.imshow("img", img1)
cv2.waitKey()
cv2.destroyAllWindows()