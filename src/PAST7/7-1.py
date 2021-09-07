from collections import deque

N, M = map(int,input().split())

edges = [[] for _ in range(N)]  #繋がってる道を保存

for _ in range(M):
    u, v = map(int,input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

s = int(input())
s -= 1
K = int(input())
T = list(map(int,input().split()))
for i in range(K):
    T[i] -= 1

T.append(s)  #T[K]に始点sを入れておく

Dist = []   #dist[k][l]にT[k]からT[l]までのコストを保存していく
for t1 in T:
    dist = [float('inf')] * N
    Q = deque()
    Q.append(t1)
    dist[t1] = 0
    while len(Q) > 0:
        i = Q.popleft()
        for j in edges[i]:
            if dist[j] == float('inf'):
                dist[j] = dist[i] + 1
                Q.append(j)

    res = []
    for t2 in T:
        res.append(dist[t2])     #t1を始点としたときのそれぞれの道までの距離を配列で記録

    Dist.append(res)


#集合を使用
#cost[n][i]　Tの中で訪れた頂点の集合がnで、最後に訪れた頂点がiの時の最小コスト(6-5-3参照)

ALL = 1<<K
cost = [ [float('inf')] * K for _ in range(ALL)]

for i in range(K):
    cost[1<<i][i] = Dist[K][i]
#cost[1<<i][i]に、始点をiとして他のtを順に回る時の初期値としてDist[k][i]（本当の始点sからiまでの距離）を入れておく

def has_bit(n, i):
    return ((n|1<<i) > 0)

for n in range(ALL):
    for i in range(K):
        for j in range(K):
            if has_bit(n, j) or i == j:
                continue
            else:
                cost[n|1<<j][j] = min(cost[n|1<<j][j], cost[n][i] + Dist[i][j])

#終点はどこでもいいので、k個全て訪問した時の最小コストが答え
print(min(cost[ALL-1]))
