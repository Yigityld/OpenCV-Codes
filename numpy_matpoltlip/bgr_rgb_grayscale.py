import cv2
import matplotlib.pyplot as plt


img = cv2.imread("smile.jpg", 0)
"""
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
"""
plt.imshow(img, cmap="gray", interpolation="BICUBIC")
plt.show()
