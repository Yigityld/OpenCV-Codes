import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
y = x
print(x)
print(y)

# plt.plot(x, y)
plt.plot(x, y, "o--")
# o, o-, o--
plt.plot(x, -y)
plt.plot(-x, y, "o")
plt.title("Grafik")
plt.show()
