print("Please input 3 sides of a triangle in a line: ")
a,b,c=map(int,input().split())
p=(a+b+c)/2
print('- Perimeter of the triangle is',p*2)
print('- Area of the triangle is',(p*(p-a)*(p-b)*(p-c))**(1/2))