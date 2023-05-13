import cv2
import numpy as np

img1 = cv2.imread("bitwise_1.png")
img2 = cv2.imread("bitwise_2.png")

bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_xor = cv2.bitwise_xor(img1, img2)
bit_not = cv2.bitwise_not(img1)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("Bitwise and:", bit_and)
cv2.imshow("Bitwise or:", bit_or)
cv2.imshow("Bitwise xor:", bit_xor)
cv2.imshow("Bitwise not:", bit_not)
cv2.waitKey()
cv2.destroyAllWindows()
