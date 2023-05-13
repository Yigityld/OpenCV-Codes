import cv2
import numpy as np

img_filter = cv2.imread("filter.png")
img_bilateral = cv2.imread("bilateral.png")
img_median = cv2.imread("median.png")

# bulanık yapıyor
blur = cv2.blur(img_filter, (5, 5))
blur_g = cv2.GaussianBlur(img_filter, (5, 5), cv2.BORDER_DEFAULT)
blur_m = cv2.medianBlur(img_median, 5)
blur_b = cv2.bilateralFilter(img_bilateral, 9, 75, 75)

# 5 olan kısım hep poz tek sayı olmalı
cv2.imshow("blur_b=", blur_b)
cv2.imshow("Blur_m=", blur_m)
cv2.imshow("Blur2=", blur_g)
cv2.imshow("Blur=", blur)
cv2.imshow("Original=", img_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
