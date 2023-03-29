# 버블정렬 ========================================================================================
def bubble_sort(lst, rev = False):
    for i in range(1, len(lst)):
        for j in range(len(lst) - i):
            if lst[j] < lst[j+1] and rev:
                lst[j+1], lst[j] = lst[j], lst[j+1]
            elif lst[j] > lst[j+1] and not rev:
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst

# 카운팅 정렬 ========================================================================================
def Counting_sort(A, k):
    # A[] 입력배열 0 to k
    # B[] 정렬된 배열
    # C[] 카운트 배열
    B = [0] * len(A)
    C = [0] * (k+1)
    for i in range(0, len(A)):  # 각 값 개수 세기
        C[A[i]] += 1
    
    for i in range(1, len(C)):  # 누적합
        C[i] += C[i - 1]
    
    for i in range(len(B) - 1, -1, -1):  # 개수 빼고 그 위치에 삽입
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    return B

# 셀렉션 정렬 ========================================================================================
## a:리스트, N:리스트 길이
def selection_sort(a, N):
    for i in range(N-1):
        minIdx = i  # 최소인덱스 정의
        for j in range(i+1, N):  # 최소인덱스 찾기
            if a[minIdx] > a[j]: 
                minIdx = j
        # 리스트에서 최소값 찾았으니 위치 바꾸기
        a[i], a[minIdx] = a[minIdx], a[i]
    return a

# 셀렉션 알고리즘
def select(arr, k):
    for i in range(0, k):  # 위와 달리 목표 k번째 까지만 선택함
        minIdx = i
        for j in range(i+1, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return arr[k-1]  # k 번째로 작은 목표값 반환

# 병합정렬 ========================================================================================
def merge(left, right):
    # 병합 알고리즘 적용
    pass

# 분할과정(수정 전)
## 배열 m을 통째로 받아서 분할
def msort(m):
    if len(m) == 1:
        return m
    mid == len(m)//2
    # 원본과 같은 크기의 배열이 또 만들어짐
    # 메모리 너무 많이 먹음
    left = m[0:mid]
    right = m[mid:]
    
    left = msort(left)
    right = msort(right)

    return merge(left, right)

# 분할, 병합과정 (수정)
## 시작과 끝 인덱스를 받음
def mergesort(s, e):
    if s==e:
        return
    
    # partition
    m = (s+e)//2
    mergesort(s, m)
    mergesort(m+1, e)

    # merge
    k = 0
    l, r = s, m+1  # 왼쪽과 오른쪽 각각 가장 작은 숫자 위치
    while l <= m or r <= e:
        if l<=m and r <=e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1
                k += 1
            else:
                tmp[k] = arr[r]
                r += 1
                k += 1
        elif l <= m:
            tmp[k] = arr[l]
            l += 1
            k += 1
        elif r <= e:
            tmp[k] = arr[r]
            r += 1
            k += 1
    
    # tmp에 저장된 배열 원본 배열에 복사
    i = 0
    while i<k:
        arr[s+i] = tmp[i]
        i += 1
    return

# 퀵 정렬 ========================================================================================
# A 는 원본 배열
def hoare(A, l, r):
    pivot = A[l]  # 맨 왼쪽원소 pivot
    i = l  # 피봇보다 큰 값을 찾아 오른쪽 이동
    j = r  # 피봇보다 작은 값을 찾아 왼쪽 이동
    while i<=j:
        while i<=j and A[i] <= pivot:
            i += 1
        while i<=j and A[j] >= pivot:
            j -= 1
        if i < j:  # 교차하지 않은 경우
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def qsort(A, l, r):
    if l < r:
        s = hoare(A, l, r)
        qsort(A, l, s-1)
        qsort(A, s+1, r)