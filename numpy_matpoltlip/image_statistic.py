
import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("smile.jpg")
plt.imshow(img)
plt.show()

print(img.min())
print(img.max())
print("ort", img.mean())
print("meadian:", np.median(img))
print("avergae", np.average(img))
