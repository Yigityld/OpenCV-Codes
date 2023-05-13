import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]], np.uint8)
print(x)
print(type(x))

print(x[0][0]); print(x[1][2])
print(x[:, 0])
