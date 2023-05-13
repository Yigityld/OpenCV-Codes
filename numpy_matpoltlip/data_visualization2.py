
import matplotlib.pyplot as plt


path = "coins.jpg"
img = plt.imread(path)
plt.imshow(img)
plt.show()
print(type(img))
print(img.shape)
print(img.ndim)
print(img.size)
print(img.dtype)
# r g b düşün
print("red:", img[50, 50, 0])
