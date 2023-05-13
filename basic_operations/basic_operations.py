import cv2
img = cv2.imread("klon.jpg")

dimension = img.shape
print(dimension)

color = img[420, 500]


blue = img[420, 500, 0]
green = img[420, 500, 1]
red = img[420, 500, 2]

print(blue, green, red)
print("blue:", blue)
print("green", green)
print("red", red)

img[420, 500, 0] = 250
print("New blue:", img[420, 500, 0])

blue1 = img.item(150, 200, 0)
img.itemset((150, 200, 0), 172)

print("Blue::", img[150, 200, 0])

cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()
