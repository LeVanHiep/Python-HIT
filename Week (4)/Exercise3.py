N = int(input())
A = {}
MAX=0
for i in range(N):
	X=input()
	if X in A: A[X]+=1
	else: A[X]=1
	if MAX<A[X]:
	    MAX=A[X]
	    Max=X
print(Max)