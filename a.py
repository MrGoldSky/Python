import numpy as np
 
a = input()
a = np.array(list(a))
 
_, cnt = np.unique(a, return_counts=True)
p = cnt/np.sum(cnt)
 
H = -np.sum(p * np.log2(p))
 
print(round(H, 2))