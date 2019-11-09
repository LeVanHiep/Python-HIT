N=int(input())
A=list(map(int,input().split()))
for i in range(1,N):
	A[i]+=A[i-1]
MAX=9999999999999999999999999999
Max=0
for i in range(len(A)):
    print(A[i],A[N-1]-A[i])
    if abs(A[N-1]-2*A[i])<MAX:
        MAX=abs(A[N-1]-2*A[i])
print(MAX)