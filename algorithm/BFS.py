'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(v, n):
    visited = [0] * (n+1)  # 방문 확인용 리스트 생성
    queue = [v]
    visited[v] = 1
    while queue:
        t = queue.pop(0)  # t는 현재 검사 지점
        ### visit(t)  할거 하고
        print(t, end=' ')
        ###
        for i in adjL[t]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[t] + 1  # 처음 정점에서부터의 거리 저장
    print()
    print(visited)  # 방문 확인, 거리 표시

v, e = map(int, input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(v+1)]
for i in range(e):  # 인덱스에 연결된 정점 저장
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)

bfs(3,v)



