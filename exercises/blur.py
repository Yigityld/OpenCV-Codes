import cv2


img1 = cv2.imread("starwars.jpg")
# 7 artarsa laplacian düşer
blur_image = cv2.medianBlur(img1, 25)

# blurlu olmazsa 900 veriyor
laplacian = cv2.Laplacian(blur_image, cv2.CV_64F).var()

if laplacian < 500:
    print("blur")
print(laplacian)

cv2.imshow("original", img1)
cv2.imshow("blur", blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()