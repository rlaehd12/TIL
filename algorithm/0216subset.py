key = 6
a = 6
A = [i for i in range(a)]
N = len(A)
bit = [0] * N  # bit[i] A[i]원소가 부분집합에 포함되는지 표시
cnt = 0

# 재귀 함수 활용
def subset(i,k):  # bit[i]를 결정할 함수
    if i == k:  # base case, 비트 모든 원소 결정됨
        for j in range(k):
            if bit[j]:
                print(A[j], end=' ')
        print()
    else:
        bit[i] = 1
        subset(i+1, k)
        bit[i] = 0
        subset(i+1, k)

subset(0, N)

# 예제들, 백트래킹
# 1~10 의 파워셋중 원소의 합이 10인 부분집합을 구해라
def f(i, k, key):
    if i == k:  # 하나의 부분집합 완성
        s = 0
        for j in range(k):
            if bit[j]:
                # print(A[j], end=' ')
                s += A[j]
        # print(bit, s)
        if s == key:  # 합이 키와 같으면 출력
            for j in range(k):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    else:
        bit[i] = 1
        f(i+1, k, key)
        bit[i] = 0
        f(i+1, k, key)

# f(0, N, key)

print('###################')
# 부분집합 합이 키와 같으면 1을 반환
def f_re(i, k, key):
    if i == k:  # 하나의 부분집합 완성
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]
        if s == key:
            return 1
        return 0

    # if i == k:  # base case, 배열 크기만큼 오면 확인
    #     if s == t:
    #         # for j in range(k):  # 출력용 코드
    #         #     if bit[j]:
    #         #         print(A[j], end=' ')
    #         # print()
    #         cnt += 1
    #     return
    else:
        bit[i] = 1
        if f_re(i+1, k, key):
            return 1
        bit[i] = 0
        if f_re(i+1, k, key):
            return 1
        return 0

bit = [0] * N
a = f_re(0, N, key)
print(a)

print('###################')
# 백트래킹, 부분집합 합이 목표보다 크면 고려할 필요 없음
# 가지치기 시행
# i원소, k집합 크기, s i-1까지 고려된 합, t 목표
def f_back(i, k, s, t, rs): 
    global cnt
    global fcnt
    fcnt += 1  # 함수 호출시마다 +1

    #  가지치기=========================
    if s > t:  # 이미 합이 목표값보다 크면
        return 
    # 남은 원소 고려할 필요 없는 경우
    elif s == t:  # 이미 목표와 같으면
        cnt += 1
        print(bit)
        return
    elif s+rs <key:  # 나머지 원소 고려해도 답에 도달 못하면
        return

    elif i == k:  # 모든 원소 고려
        return

    else:
        bit[i] = 1
        f_back(i+1, k, s+A[i], t, rs-A[i])  # A[i]포함
        bit[i] = 0
        f_back(i+1, k, s+0, t, rs-A[i])  # A[i] 미포함

bit = [0] * N
fcnt = 0
f_back(0, N, 0, key, sum(A))
print(cnt, fcnt)  # 목표 개수, 함수 호출 횟수
