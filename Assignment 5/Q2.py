import numpy as np

#(a)
arr = np.array([10, 52, 62, 16, 16, 54, 453])
# i
print(np.sort(arr))
# ii
print(np.argsort(arr))
# iii
print(np.sort(arr)[:4])
# iv
print(np.sort(arr)[-5:])


#(b)
arr2 = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
# i
print(arr2[arr2 == arr2.astype(int)])
# ii
print(arr2[arr2 != arr2.astype(int)])