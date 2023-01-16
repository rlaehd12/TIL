'''# change 임시 변수 활용 or'''
x, y = 10, 20

y, x = x, y

print(x,y)

'''# 메모리 주소 찾기'''
age = 10
memory_addr = id(age)
# print(memory_addr)

'''주소값 확인'''
a=[]
b=[]
c=a # c a의 주솟값을 준것.(참조)
# print(id(a))
# print(id(b))
# print(id(c))

result = (a is b)
# print(result)
result = (a is c)
# print(result)
result = (b is c)
# print(result)

''' true false'''
b=[]
if not b:
    print('b는 빔')

'''리스트'''

a=[a,b,c]
print(len(a))