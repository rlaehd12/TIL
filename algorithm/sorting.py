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
    for i in range(0, len(A)):
        C[A[i]] += 1
    
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    
    for i in range(len(B) - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    return B

a = [1,2,64,4,32,41,54]
#bubble_sort(lst, rev= True)
print(Counting_sort(a,max(a)))
