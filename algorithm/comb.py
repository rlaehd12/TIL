N = 5
# 평범한 반복 구조
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(i, j, k)

# 재귀 이용
# A[] 원본 배열
def nCr(n,r,s):
    if r== 0:
        print(comb)
    else:
        for i in range(s,n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)

n = 5
r = 3
comb = [0]*3
A = [i for i in range(n)]
nCr(n, r, 0)

print()
# 다른 재귀 이용 방법
# tr - 저장할 배열
# an - 원본 배열
def comb(n, r):
    if r==0:
        print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = an[n-1]
        comb(n-1, r-1)  # 순서 무조건 지켜야 함
        comb(n-1, r)
tr = [0]*3
an = A
comb(n, r)