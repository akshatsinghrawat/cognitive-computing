import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y1, y2, y3, y4 = x**2, np.sin(x), np.exp(x), np.log(np.abs(x) + 1)
plt.plot(x, y1, label="x^2")
plt.plot(x, y2, label="sin(x)")
plt.plot(x, y3, label="e^x")
plt.plot(x, y4, label="log(|x|+1)")
plt.legend()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Function Plots")
plt.show()