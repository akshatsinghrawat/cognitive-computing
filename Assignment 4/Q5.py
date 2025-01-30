import numpy as np


ucs420_akshat = np.array([[10, 20, 30, 40],[50, 60, 70, 80],[90, 15, 20, 35]])

print("Original Array (ucs420_akshat):\n", ucs420_akshat)

mean_value = np.mean(ucs420_akshat)
median_value = np.median(ucs420_akshat)
max_value = np.max(ucs420_akshat)
min_value = np.min(ucs420_akshat)
unique_elements = np.unique(ucs420_akshat)

print("Mean of the array:", mean_value)
print("Median of the array:", median_value)
print("Max value in the array:", max_value)
print("Min value in the array:", min_value)
print("Unique elements in the array:", unique_elements)


reshaped_ucs420_akshat = ucs420_akshat.reshape((4, 3))
print("\nReshaped Array (reshaped_ucs420_akshat):\n", reshaped_ucs420_akshat)


resized_ucs420_akshat = ucs420_akshat.resize((2, 3))
print("\nResized Array (resized_ucs420_akshat):\n", ucs420_akshat)
