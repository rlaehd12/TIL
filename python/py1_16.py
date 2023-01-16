# change 임시 변수 활용 or
x, y = 10, 20

y, x = x, y

print(x,y)

# 메모리 주소 찾기
age = 10
memory_addr = id(age)
print(memory_addr)