import numpy as np
A = np.random.random(10)
print(A)
x=max(A)
for i in range(len(A)):
	if A[i]==x: A[i]=0
print(A) 