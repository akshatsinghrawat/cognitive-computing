import numpy as np

# a
X = sum(map(ord, "AB"))
s = np.array([X + 50*i for i in range(5)], dtype=float)

# b
r = ((X % 5) + 5) / 100
st = s * (1 + r)

# c
d = np.where(s < X + 100, 0.95, 0.90)
sf = st * d
print(sf)

# d
w = np.tile(sf, (3, 1))
w = w * (1.02 ** np.arange(3))[:, None]
print(w)