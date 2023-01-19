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
    print('b는 비어있음')

'''리스트'''
print(list(range(6,1,-1)))

'''슬라이싱'''
print([1,2,3,4][0:4:2]) #[1,3]
print((1,2,3,4,5,)[0:4:2]) #(1,3)
print('abcdefg'[1:4:2]) #'bd'

'''딕셔너리'''
dict_a = {'a': 'apple', 'b':'banana', 'list':[1,2,3]}
# print(dict_a['c']) 이렇게 쓰면 오류남 c라는 키가 없어서
print(dict_a.get('c')) # get을 쓰면 없는 키는 none 반환
