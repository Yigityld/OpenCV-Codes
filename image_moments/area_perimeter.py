import cv2

img = cv2.imread("contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thres = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contur, ret = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contur[0]
M = cv2.moments(cnt)
area = cv2.contourArea(cnt)
perimeter = cv2.arcLength(cnt, True)

print(area)
print(M["m00"])
print(perimeter)
cv2.drawContours(img, contur, -1, (0, 255, 255), 3)
cv2.imshow("image", img)
cv2.waitKey()

cv2.destroyAllWindows()








































"""import cv2

img = cv2.imread("contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
#bu da çözüm
M = cv2.moments(cnt)
# bu da çözüm
area = cv2.contourArea(cnt)
# çevre
perimeter = cv2.arcLength(cnt,True)
print(perimeter)
print(area)
print(M["m00"])
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

cv2.imshow("original", img)
cv2.waitKey()
cv2.destroyAllWindows()"""

