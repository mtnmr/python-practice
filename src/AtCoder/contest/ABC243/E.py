N, M = map(int,input().split())
es = []
for _ in range(M):
    a,b,c = map(int,input().split())
    es.append((a-1, b-1, c))

d = [ [float("inf")] * N for _ in range(N)]
#ワーシャルフロイドで任意の２頂点間の距離を計算する
for a, b, c in es:
    d[a][b] = c
    d[b][a] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = 0
for a, b, c in es:
    unused = 0
    for i in range(N):
        if d[a][i] + d[i][b] <= c:
            unused = 1
    ans += unused
print(ans)




# N, M  = map(int,input().split())

# G = [[] for _ in range(N)]
# for _ in range(M):
#     a, b, c = map(int,input().split())
#     G[a-1].append((b-1, c))
#     G[b-1].append((a-1, c))



# def dijkstra(s, n, M):
#     import heapq 

#     visited = [False] * n
#     dist = [float('inf')] * n

#     dist[s] = 0

#     Q = []
#     heapq.heappush(Q, (dist[s], s))

#     while len(Q) > 0:
#         d, u = heapq.heappop(Q)
#         if visited[u]:
#             continue
#         visited[u] = True
#         for v, c in M[u]:
#             if dist[u] + c < dist[v]:
#                 dist[v] = dist[u] + c
#                 heapq.heappush(Q, (dist[v], v))

