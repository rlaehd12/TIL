'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preorder(i):
    if i > 0:  # 존재하는 정점이면
        print(i, end= ' ')
        preorder(left[i])
        preorder(right[i])

# v = int(input())
# arr = list(map(int, input().split()))
# e = v-1
# left = [0] * (v+1)  # 왼쪽 오른쪽 연결 노드
# right = [0] * (v+1)

# # 자식을 인덱스로 부모 저장
# par = [0] * (v+1)

# for i in range(e):
#     p, c = arr[i*2], arr[i*2+1]
#     if left[p] == 0:
#         left[p] = c
#     else:
#         right[p] = c
#     par[c] = p

# root = 1
# # 부모가 있으면(자식 인덱스에 저장된 값이 있으면) 다음 노드 찾아봄
# while par[root] != 0:
#     root += 1

# preorder(root)

################## heap
# 최대 100개의 key
# 최대힙

def enq(n):
    global last
    last += 1  # 완전이진트리에 마지막 정점 추가
    heap[last] = n
    # 부모 있고, 자식이 부모보다 크면 교환
    c = last
    p = c//2
    while p>0 and heap[c]>heap[p]:
        heap[c], heap[p] = heap[p], heap[c]
        c = p
        p = c//2


def deq():
    global last
    return_val = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p*2
    while c <= last:
        # 오른쪽 자식이 있는데 오른쪽이 왼쪽보다 크면
        if c+1 <= last and heap[c] < heap[c+1]:  
            c += 1  # 비교대상 오른쪽으로 변경
        
        if heap[c] > heap[p]:
            heap[c], heap[p] = heap[p], heap[c]
        else:
            break
        
        p = c
        c = p*2


    return return_val


#========================================================최소 힙 클래스 구현
class stack():

    def __init__(self, n):
        self.lst = [0] * n
        self.top = -1
        self.size = n
    
    def isempty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def push(self, item):
        self.top += 1
        self.lst[self.top] = item
    
    def pop(self):
        if self.isempty():
            pass
        else:
            self.top -= 1
            return self.lst[self.top + 1]
    
    def peek(self):
        if self.isempty():
            pass
        else:
            return self.lst[self.top]

class heap(stack):  # 최소 힙

    def __init__(self, n):
        super().__init__(n+1)
        self.top = 0
    
    def isempty(self):
        if self.top == 0:
            return True
        else:
            return False
    
    def enq(self, n):
        self.push(n)
        c = self.top
        p = c//2
        while p > 0 and self.lst[c] < self.lst[p]:
            self.lst[c], self.lst[p] = self.lst[p], self.lst[c]
            c = p
            p = c//2
    
    def deq(self):
        if self.isempty():
            return

        temp = self.lst[1]
        self.lst[1] = self.pop()

        p = 1
        c = p*2

        while c <= self.top:
            if c+1 <= self.top and self.lst[c] > self.lst[c+1]:
                c += 1
            
            if self.lst[c] < self.lst[p]:
                self.lst[c], self.lst[p] = self.lst[p], self.lst[c]
            else:
                break

            p = c
            c = p*2
        return temp