import numpy as np

x = np.empty([3, 3], np.uint8)
print(x)

y = np.full((3, 3, 3), dtype=np.int16, fill_value=45)
print(y)
print("---------------------------")

z = np.ones((2, 7, 5), dtype=np.uint8)
print(z)
print("sssssssssssssssssss");print("--------------")
r = np.zeros((3, 6, 4), dtype=np.uint8)
print(r)
