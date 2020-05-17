import numpy as np
x = np.random.randint(0, 100, 20)
y = np.random.uniform(0, 20)
print(x)
print(y)
print(abs(min([abs(y-i) for i in x])))
Min = 0
for i in range(len(x)):
	if abs(x[Min]-y)>abs(x[i]-y): Min=i
print(Min)