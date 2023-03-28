p = [0,1,2,3]
N = len(p)

# 순열
# 자리를 바꿔가며 구현
# i 값을 결정할 자리, k 결정할 개수
def f(i, k):
    if i == k:  # base case, 전체 크기 도달
        # 수행할 작업 작성
        print(p)  
    else:
        # (자신부터) 오른쪽 원소들과 교환
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]  # 서로 자리 바꿈
            # 현재 p[i] 결정됨, 관련 작업 가능
            f(i+1, k)
            p[i], p[j] = p[j], p[i]  # 다시 원상복구

# f(0, N)

# 사용했나 안했나 방법
A = [1, 4, 5]  # 원본 배열
p = [0] * 3  # 출력 목록
used = [0] * 3  # 사용하지 않은 숫자 목록


def perm(i, k):
    if i == k:
        print(p)
    else:
        for j in range(k):    # 사용하지 않은 숫자
            if used[j] == 0:  # used에서 순서대로 검색
                p[i] = A[j]
                used[j] = 1  # j번 자리 숫자 사용했다 표시
                perm(i+1, k)
                used[j] = 0  # j번 자리 원상복귀

perm(0, 3)