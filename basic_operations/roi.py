# roi=region of interest

import cv2

img = cv2.imread("klon.jpg")

roi = img[33:190, 210:360]
dimension = img.shape
print(dimension)

cv2.imshow("image", img)
cv2.imshow("ROİ:", roi)
cv2.waitKey()
cv2.destroyAllWindows()
