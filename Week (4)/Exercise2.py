print('Moi ban nhap cac phan tu vao mang A: ')
A = list(map(int,input().split()))
print('Moi ban nhap cac phan tu vao mang B: ')
B = list(map(int,input().split()))
print('Mang tong cua A va B la: [',end='')
for i in A:
	if i in B and i not in C:
		print(i,end='')
		C.append(i)
print(']',end='')