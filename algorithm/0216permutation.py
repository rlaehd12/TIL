p = [1, 2, 3]
N = len(p)

# 순열
# 자리를 바꿔가며 구현
# i 현재 원소, k 전체 크기
def f(i, k):
    if i == k:  # base case, 전체 크기 도달
        print(p)
    else:
        # 오른쪽과 교환
        for j in range(i, k):  # i부터 배열 크기만큼
            p[i], p[j] = p[j], p[i]  # 서로 자리 바꿈
            # 현재 p[i] 결정됨, 관련 작업 가능
            f(i+1, k)
            p[i], p[j] = p[j], p[i]  # 다시 원상복구

f(0, N)