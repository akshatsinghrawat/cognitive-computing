import numpy as np

akshat = np.linspace(10, 100, 25)
print("Array:", akshat)
print("Dimensions:", akshat.ndim)
print("Shape:", akshat.shape)
print("Total elements:", akshat.size)
print("Data type of elements:", akshat.dtype)
print("Total bytes consumed:", akshat.nbytes)

transpose_reshape = akshat.reshape((5, 5))
print("Transpose using reshape():\n", transpose_reshape)

transpose_T = akshat.T
print("Transpose using T attribute:", transpose_T)

