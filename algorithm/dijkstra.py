'''
5 9
0 1 2
0 2 4
1 2 1
2 1 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''
INF = 1000  # 문제에 맞는 큰 숫자, 파이썬 inf 너무 크기 큼


# 다익스트라는 모든 정점에 대해 최소값 구함, 중간에 못멈춤
def dijkstra(s, V):  #s 출발, V 마지막 정점 번호
    U = [0] * (V+1)  # U 최소비용이 결정된 정점 집합
    U[s] = 1

    for i in range(V+1):  # 시작 정점 비용 D에 복사
        D[i] = adjM[s][i]

    # 남은 정점 비용 결정
    N = V+1
    for _ in range(N-1):  # N-1개 정점의 비용 결정
        # D[w]가 최소인 w 결정
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i]==0 and minV > D[i]:  # 비용이 확정되지 않은 남은 정점 i중 최소
                w = i
                minV = D[i]
        U[w] = 1  # 최소인 w는 최소 비용 D[w] 확정
        # w에서 갈수 있는 모든 간선 조사
        for v in range(V+1):
            if 0< adjM[w][v] < INF:  # 자기자신이 아닌 w에 인접한 정점이면
                D[v] = min(D[v], D[w] + adjM[w][v])  # 원래 v까지 거리 VS w까지 거리 + w->v 거리

V, E = map(int, input().split())  # 0~V번 정점, 간선수, 총 정점 V+1개
adjM = [[INF]*(V+1) for _ in range(V+1)]
for i in range(V+1):
    adjM[i][i] = 0  # 자기자신 가는 비용 0으로 초기화
# 방향 있음
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w

# for i in adjM:
#     print(i)

D = [0]*(V+1)
dijkstra(0, V)
print(D)