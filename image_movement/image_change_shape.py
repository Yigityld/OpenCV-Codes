import cv2
import numpy as np

img = cv2.imread("klon.jpg", 0)

row, col = img.shape

M = np.float32([[1, 0, 100], [0, 1, 100]])

dst = cv2.warpAffine(img, M, (row, col))

cv2.imshow("dsr", dst)
cv2.waitKey()
cv2.destroyAllWindows()
