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

## 딕셔너리 활용
graph = {}

graph[0] = [1,2]
graph[1] = [2,3]
##......

# 재귀 구현
def dfs1(v):
	visited[v] = 1
	print(v, end = " ")
	# 현재 v는 시작정점, 인접한 정점 중 방문을 안한 곳 
	for w in range(1, V+1):
		if arr[v][w] == 1 and visited[w] == 0:
			dfs(w)

def dfs2(v):
    stack = [v]
    # 스택이 빌 때까지 반복 
    while len(stack):
        v = stack.pop()
        # v가 아직 방문 전이라면 
        visited[v] = 1

        for w in range(1, V + 1):
            if arr[v][w] == 1 and visited[w] == 0:
                stack.append(w)


dfs1(1)
