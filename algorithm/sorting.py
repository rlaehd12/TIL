def bubble_sort(lst, rev = False):
    for i in range(1, len(lst)):
        for j in range(len(lst) - i):
            if lst[j] < lst[j+1] and rev:
                lst[j+1], lst[j] = lst[j], lst[j+1]
            elif lst[j] > lst[j+1] and not rev:
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst

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


def selection_sort(a, N):
    for i in range(N-1):
        minIdx = i  # 최소인덱스 정의
        for j in range(i+1, N):  # 최소인덱스 찾기
            if a[minIdx] > a[j]: 
                minIdx = j
        # 리스트에서 최소값 찾았으니 위치 바꾸기
        a[i], a[minIdx] = a[minIdx], a[i]
    return a

## 셀렉션 알고리즘
def select(arr, k):
    for i in range(0, k):  # 위와 달리 목표 k번째 까지만 선택함
        minIdx = i
        for j in range(i+1, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return arr[k-1]  # k 번째로 작은 목표값 반환