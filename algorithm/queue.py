# 기본 구조
def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data


def dequeue():
    global front
    front += 1
    return queue[front]

queue = [0]*6
front = rear = -1

enqueue(5)
enqueue(3)
print(dequeue())
print(dequeue())

## 그냥 리스트 사용, 비효율적이긴 한데 편함

lst = []
lst.append(12)
lst.append(23)
lst.append(34)
print(lst.pop(0))
print(lst.pop(0))
print(lst.pop(0))

## 혹은 deque 사용 / 그냥 리스트로 하는것보다는 빠름

from collections import deque

q1 = deque()
q1.append(10)
q1.append(23)
q1.append(34)
print(q1.popleft())
print(q1.popleft())
print(q1.popleft())
