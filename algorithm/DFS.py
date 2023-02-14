''' 입력예시
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

v, e = map(int, input().split())
arr = list(map(int, input().split()))
# edge 저장
## 행렬형태, 인접행렬
adjm = [[0]*(v+1) for _ in range(v+1)]
for i in range(e):
    v1, v2 = arr[i*2], arr[i*2+1]
    adjm[v1][v2] = 1
    adjm[v2][v1] = 1
## 리스트, 인덱스에 연결된 정점 저장, 인접리스트
adjl = [[] for _ in range(v+1)]
for i in range(e):
    v1, v2 = arr[i*2], arr[i*2+1]
    adjl[v1].append(v2)
    adjl[v2].append(v1)

print(adjl)
for i in adjm:
    print(i)