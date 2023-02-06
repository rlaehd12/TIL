## 델타이용 2차원 서치

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

result = (9>>1)
print(result)