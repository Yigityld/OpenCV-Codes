
import cv2

img = cv2.imread("contour.png")
cv2.imshow("img", img)
edges = cv2.Canny(img, 100, 200)
cv2.imshow("cany", edges)
cv2.waitKey()
cv2.destroyAllWindows()