N=int(input())
A=list(input().split())
for i in A:
    C=1
    L=len(i)
    K=(L-1)//2
    for j in range(K+1):
        if i[j]!=i[L-j-1]: C=0
    if C: print(i,end=' ')