import random
A=list(map(int,input().split()))
random.shuffle(A)
N=(len(A)*7)//10
print(A[:N],A[N:])