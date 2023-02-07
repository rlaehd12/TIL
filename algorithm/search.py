## 델타이용 2차원 탐색

di = [0, 1, 0, -1]  # 우하좌상
dj = [1, 0, -1, 0]
n = 3
for i in range(n):
    for j in range(n):
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<n and 0<=nj<n:
                #print(i, j, ni, nj)
                pass


### 순차검색 정렬안됨
def sequentialSearch(a, n, key):
    # a 값 찾을 리스트
    # n 리스트 길이
    # key 값
    i = 0
    while i<n and a[i] != key:  # 단축평가, 유효범위 밖이면 일단 멈춤
        i += 1
    if i <n: return i  # a[i] == key 여서 반복문 빠졌으면
    else: return -1  # i<n이 아니게 되어서 반복문 빠졌으면


### 순차검색 정렬됨
def sequentialSearch2(a, n, key):
    i = 0
    while i<n and a[i] < key:  # 범위 안, 키값보다 작으면 계속
        i += 1
    if i <n and a[i] == key:  # 그 전에 찾으면 값 리턴
        return i
    else: return -1 # 범위 밖, 키값보다 커지면 -1 리턴

### 이진 검색
def binarySearch(a, n, key):
    # a 값 찾을 리스트
    # n 리스트 길이
    # key 값
    start = 0
    end = n-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:  # 검색 성공
            return True
        elif a[middle] > key:  # 중앙이 목표보다 더 큼
            end = middle - 1
        else:                  # 중앙이 목표보다 작음
            start = middle + 1
    return False  # 검색 실패

## 이진 검색 재귀함수

def binarySearch2(a, low, high, key):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]:
            return True
        elif a[middle] > key:
            return binarySearch2(a, low, middle - 1, key)
        elif a[middle] < key:
            return binarySearch2(a, middle + 1, high, key)
