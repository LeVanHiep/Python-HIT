A1,A2,A3,A4 = 1,1,3,3#list(map(int,input().split()))
B1,B2,B3,B4 = 2,2,4,4#list(map(int,input().split()))
print((A3-A1)*(A4-A2)+(B3-B1)*(B4+B2)-(A3-B1)*(A4-B2))