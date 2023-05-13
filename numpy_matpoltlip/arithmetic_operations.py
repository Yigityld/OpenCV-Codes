
import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("map.jpeg")

plt.subplot(4, 2, 1)
plt.title("Original")
plt.imshow(img)
plt.subplot(4, 2, 2)
plt.title("img + img")

plt.imshow(img + img)

plt.subplot(4, 2, 3)
plt.title("img - img")
plt.imshow(img - img)

plt.subplot(4, 2, 6)
plt.title("np.flit 2")
plt.imshow(np.flip(img, 2))
# 0, 1, 2 yansıtma yapar x,y ,z gçre

plt.subplot(4, 2, 4)
plt.title("np.flit 0")
plt.imshow(np.flip(img, 0))

plt.subplot(4, 2, 5)
plt.title("np.flit 1")
plt.imshow(np.flip(img, 1))

plt.subplot(4, 2, 7)
plt.title("np.fliplr")
plt.imshow(np.fliplr(img))

plt.subplot(4, 2, 8)
plt.title("np.flip.ud")
plt.imshow(np.flipud(img))

plt.show()
