N = 6
# findset
def find_set(x):  # x가 속한 집합의 대표원소 반환
    while x != rep[x]:  # x==rep[x] 될 때 까지
        x = rep[x]
    return x

# unionset
def union(x, y):  # y의 대표원소가 x의 대표원소를 가리키게 함
    rep[find_set(y)] = find_set(x)

# makeset
rep = [i for i in range(N)]

# MST(Kruskal) ===========================================
'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
V, E = map(int, input().split())  # v개의 정점, E개의 간선 정보
rep = [i for i in range(V+1)]  # makeset
graph = []
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph.append([v1, v2, w])

# [1] 가중치 기준 오름차순 정렬
graph.sort(key= lambda x: x[2])

# [2] N개 정점(v+1), N-1 개의 간선 선택
N = V + 1
s = 0
cnt = 0
for u, v, w in graph:
    if find_set(u) != find_set(v):  # 사이클이 생기지 않는다면
        cnt += 1
        s += w
        union(u, v)
        if cnt == N-1:
            break


# prim===================================
import heapq

def prim(graph, start):
    heap = list()

    connected = [False] * (N+1)
    sum_w = 0
    heapq.heappush(heap, (0, start))

    # 우선순위 큐 빌때까지
    while heap:
        weight, v = heapq.heappop(heap)
        if not connected[v]:
            connected[v] = True
            sum_w += weight
            for i in range(1, N+1):
                if (graph[v][i] != 0) and (not connected[i]):
                    heapq.heappush(heap, (graph[v][i], i))
    print(sum_w)

N = 3
graph = [[0] * (N+1) for _ in range(N+1)]  # matrix
root = list(range(N+1))
graph[1][2], graph[1][3] = 2, 12
graph[2][1], graph[2][3] = 2, 5
graph[3][1], graph[3][2] = 4, 5
prim(graph, 1)
