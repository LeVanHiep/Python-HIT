import numpy as np
x = np.array([1,2,0,0,4,0])
for i in range(len(x)):
	if x[i]: print(i,end=', ')