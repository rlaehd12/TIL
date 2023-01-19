'''입력 받아서 홀짝 여부 판별'''
# num = int(input())
# if num % 2: # if num % 2 == 1 ## 1은 True
#     print('홀')
# else:
#     print('짝')

'''조건 표현식'''
# 홀짝 구분 조건표현식으로
num = 124
result = '홀' if num % 2 else '짝'
print(result)

'''for문 문자열 순회, 딕셔너리 순회'''
# chars = input()

# for char in chars:
#     print(char)

# grades = {'a': 80, 'b': 90, 'c': 83}
# for student in grades:
#     print(student,grades[student])

# for student, grade in grades.items(): #딕셔너리.items = 튜플로 키, 값을 넘겨줌 
#     print(student, grade)

'''enumerate'''
members = ['a','b','c']
for idx, number in enumerate(members):
    print(idx,number)

'''list comprehension'''
# cubic = []
# for number in range(1,4):
#     cubic.append(number ** 3)
# print(cubic)

cubic_list = [number ** 3 for number in range(1,4)]
print(cubic_list)

'''dict comprehension'''
# cubic = {}
# for number in range(1,4):
#     cubic[number] = number ** 3
# print(cubic)

cubic_dict = {number: number ** 3 for number in range(1,4)}
print(cubic_dict)