import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
M=int(input("Enter a value:"))
x=np.linspace(-10, 10,20)
y1=M*x**2
y2=M*np.sin(x)
plt.figure(figsize=(8, 8))
plt.plot(x, y1, label=r'y=Mx^2', color='b', linestyle='--')
plt.plot(x, y2, label=r'y=M sin(x)', color='r', linestyle='-')
plt.grid(True)
plt.legend()
plt.title('PLots of y=Mx^2 and y=Msin(x)')
plt.show()
