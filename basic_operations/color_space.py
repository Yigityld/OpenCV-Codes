import cv2

img = cv2.imread("klon.jpg")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("KLON.rgb", img_rgb)
cv2.imshow("KLON.hsv", img_hsv)
cv2.imshow("Klon", img)
cv2.imshow("Klon.gri", img_gray)
cv2.waitKey()
cv2.destroyAllWindows()
