import numpy as np

x = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], np.uint8)
print(x)
print(type(x))
print(x[1][0][2])
print(x[1, 1, 1])
