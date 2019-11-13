print('Moi ban nhap cac phan tu vao mang A: ')
A = list(map(int,input(),split()))
print('Moi ban nhap cac phan tu vao mang B: ')
B = list(map(int,input(),split()))
print('Mang tong cua A va B la: ')
for i in range(len(A)):
	print(A[i]+B[i],end=' ')