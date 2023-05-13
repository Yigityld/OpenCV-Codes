import cv2
import numpy as np

img = cv2.imread("star.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, 0)
contur, ret = cv2.findContours(thresh, 2, 1)

cnt = contur[0]
hull = cv2.convexHull(cnt, returnPoints=False)

Defects = cv2.convexityDefects(cnt, hull)
for i in range(Defects.shape[0]):
    s, e, f, d = Defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, (0,0,255), 3)
    cv2.circle(img, far, 3, (0, 0, 0), -1)


cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()