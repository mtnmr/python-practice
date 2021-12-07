#AIZU ALDS1-12-B 
#重みつきグラフ　単一始点最短経路　ダイクストラのアルゴリズム
#ヒープなし

def dijkstra(s, n, G):
    visited = [False] * n
    dist = [float('inf')] * n
    par = [-1] * n

    dist[s] = 0

    while True:
        mincost = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < mincost:
                mincost = dist[i]
                u = i

        if mincost == float('inf'):
            break

        visited[u] = True

        for v, c in G[u]:
            if not visited[v]:
                if dist[u] + c < dist[v]:
                    dist[v] = dist[u] + c
                    par[v] = u

        #隣接行列なら
        # for v in range(n):
        #     if (visited[v] == False) and (M[u][v] != -1):
        #         if (d[u] + M[u][v]) < d[v]:
        #             d[v] = d[u] + M[u][v]
        #             p[v] = u
    
    return dist

n = int(input())
G = [ [] for _ in range(n)]
for _ in range(n):
    u_list = list(map(int,input().split()))
    u = u_list[0]
    k = u_list[1]
    for i in range(2, 2+2*k, 2):
        v = u_list[i]
        c = u_list[i+1]
        G[u].append([v, c])

#もしくは隣接行列を作る
# for i in range(n):
#   node = list(map(int,input().split()))
#   u = node[0] 
#   k = node[1]
#   for j in range(k):
#     v = node[2 + (2 * j)]
#     c = node[3 + (2 * j)]
#     M[u][v] = c

ans = dijkstra(0, n, G)

for i in range(n):
    print(i, ans[i])



