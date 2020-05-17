import numpy as np
column = 5
row = 4
A = np.ones((row,column))
A[1:-1,1:-1]=0
print(A)