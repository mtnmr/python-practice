from copy import deepcopy
import heapq

N, M, Q = map(int,input().split())
G = [ [] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int,input().split())
    G[a-1].append((b-1, c))
    G[b-1].append((a-1, c))


def dijkstra(s, n, M):

    visited = [False] * n
    dist = [float('inf')] * n

    dist[s] = 0

    Q = []
    heapq.heappush(Q, (dist[s], s))

    while len(Q) > 0:
        d, u = heapq.heappop(Q)
        if visited[u]:
            continue
        visited[u] = True
        for v, c in M[u]:
            if dist[u] + c < dist[v]:
                dist[v] = dist[u] + c
                heapq.heappush(Q, (dist[v], v))

    return dist


dist = dijkstra(0, N, G)

for _ in range(Q):
    G_add = deepcopy(G)
    u, v, w = map(int,input().split())
    G_add[u-1].append((v-1, w))
    G_add[v-1].append((u-1, w))
    now = dijkstra(0, N, G_add)
    if now == dist:
        print('No')
    else:
        print('Yes')

