print('Please input a number: ')
x=int(input())
n=int(x**(1/2))

print('Square numbers from 1 to',x,'are:')
for i in range(1,n+1):
	print(i*i,end=' ')