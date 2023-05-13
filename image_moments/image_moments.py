import cv2


img = cv2.imread("contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
M = cv2.moments(thresh)

X = int(M["m10"]/M["m00"])
Y = int(M["m01"]/M["m00"])
print(X, "Y:", Y)
cv2.circle(img, (X, Y), 1, (255,0,255), 1)
cv2.imshow("original", img)
cv2.waitKey()
cv2.destroyAllWindows()


















"""
import cv2


img = cv2.imread("contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
M = cv2.moments(thresh)
print(M)

X = int(M["m10"]/M["m00"])
Y = int(M["m01"]/M["m00"])
cv2.circle(img, (X, Y), 1, (0, 0, 255), -1)
print(X)
print(Y)
cv2.imshow("original", img)
cv2.waitKey()
cv2.destroyAllWindows()
"""
