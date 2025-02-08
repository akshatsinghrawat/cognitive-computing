import numpy as np 

gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
# i
print(gfg.sum())
# ii
print(gfg.sum(axis=1))
# iii
print(gfg.sum(axis=0))