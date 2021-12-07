#AIZU ALDS1-12-C
#重みつきグラフ　単一始点最短経路　ダイクストラのアルゴリズム
#ヒープあり


def dijkstra(s, n, M):
    import heapq 

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

n = int(input())
M = [ [] for _ in range(n)]
for _ in range(n):
    u_list = list(map(int,input().split()))
    u = u_list[0]
    k = u_list[1]
    for i in range(2, 2+2*k, 2):
        v = u_list[i]
        c = u_list[i+1]
        M[u].append((v, c))


ans = dijkstra(0, n, M)

for i in range(n):
    print(i, ans[i])