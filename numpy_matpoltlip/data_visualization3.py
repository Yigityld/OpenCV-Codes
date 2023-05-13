
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)

plt.plot(x, [y**2 for y in x])
plt.plot(x, [y**3 for y in x])
plt.plot(x, 2*x)
plt.plot(x, 5.2*x)
plt.legend(["x**2", "x**3", "x*2", "5.2*x"], loc="lower left")
# min max değiştirir
plt.axis([0, 2, 0, 10])
plt.grid(True)
plt.xlabel("np.arramge (3)")
plt.ylabel("f(x)")
# min max değerler verir
plt.title("Simple plot")
print(plt.axis())

plt.savefig("D:\\opencv\\plt.png")
plt.show()
