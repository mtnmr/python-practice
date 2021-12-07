#AIZU ALDS1-12-A
#最小全域木　プリムのアルゴリズム
#はじめに、適当に選んだ頂点 1 つのみを 𝑇 に含めると確定させる
#以下をすべての頂点が 𝑇 に含まれるまで繰り返す
#全ての「既に確定した頂点」から「まだ確定していない（𝑇 に含まれていない）頂点 」へ伸びる辺を全て確認して、
#最小のコストの辺 e=(u,v) を選ぶ。そして v を 𝑇 に含めることにする。
#計算量𝑂(|𝑉|**2)
#ヒープを使えば𝑂(|𝐸|log|𝑉|)

def prim(n, G):
    visited = [False] * n
    dist = [float('inf')] * n
    par = [-1] * n    #頂点vに対して、辺がどこと繋がっているか記録
    
    dist[0] = 0

    while True:
        mincost = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < mincost:
                mincost = dist[i]
                u = i

        if mincost == float('inf'):
            break

        visited[u] = True
        
        for v in range(n):
            if not visited[v] and G[u][v] != -1:
                if G[u][v] < dist[v]:
                    dist[v] = G[u][v]
                    par[v] = u

    return sum(dist)

n = int(input())
G = []
for _ in range(n):
    g = list(map(int,input().split()))
    G.append(g)

print(prim(n,G))                    


#heapを使う例
# N = int(input())
# G = [[] for i in range(N)]
# for v in range(N):
#     for w, c in enumerate(map(int, input().split())):
#         if c != -1:
#             G[v].append((w, c))

# from heapq import heappush, heappop, heapify
# used = [0]*N
# que = [(c, w) for w, c in G[0]]
# used[0] = 1
# heapify(que)

# ans = 0
# while que:
#     cv, v = heappop(que)
#     if used[v]:
#         continue
#     used[v] = 1
#     ans += cv
#     for w, c in G[v]:
#         if used[w]:
#             continue
#         heappush(que, (c, w))
# print(ans)