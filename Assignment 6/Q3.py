import numpy as np
import matplotlib.pyplot as plt

roll_number = 102317124  
np.random.seed(roll_number)

data = np.random.randn(50)

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].plot(np.cumsum(data), color='g', linestyle='-', marker='o')
axs[0].set_title('Cumulative Sum Line Plot')
axs[0].set_xlabel('Index')
axs[0].set_ylabel('Cumulative Sum')
axs[0].grid(True)

axs[1].scatter(range(50), data, color='r', marker='x')
axs[1].set_title('Scatter Plot with Random Noise')
axs[1].set_xlabel('Index')
axs[1].set_ylabel('Value')
axs[1].grid(True)

plt.tight_layout()
plt.show()
