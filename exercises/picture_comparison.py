import cv2
import numpy as np

img1 = cv2.imread("aircraft.jpg")
img1 = cv2.resize(img1, (712, 612))

img2 = cv2.imread("aircraft1.jpg")
img2 = cv2.resize(img2, (712, 612))

img3 = cv2.medianBlur(img1, 7)

if img1.shape == img2.shape:
    print("Same size")
else:
    print("not same")
# substract iki resmi karşılatırır ve sonunda eğer farklı oldukları kısıma eklem yapar
diff = cv2.subtract(img1, img3)
b,g,r = cv2.split(diff)


if cv2.countNonZero(b) == 0:
    print("copmplitily equal")
else:
    print("not complitily euqal")
if cv2.countNonZero(r) == 0:
    print("copmplitily equal")
else:
    print("not complitily euqal")
if cv2.countNonZero(g) == 0:
    print("copmplitily equal")
else:
    print("not complitily euqal")

cv2.imshow("origi", diff)
cv2.imshow("original", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
