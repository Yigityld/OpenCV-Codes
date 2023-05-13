
import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("map.jpeg")

r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]
show = np.dstack((r, g, b))
plt.imshow(show)
plt.show()

output = [img, r, g, b]
titles = ["ımage", "red", "green", "blue"]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.axis("off")
    plt.title(titles[i])
    if i == 0:
        plt.imshow(output[i])
    else:
        plt.imshow(output[i], cmap="gray")
plt.show()

