#キューを使う
from collections import deque

N, M = map(int,input().split())

G = [ [] for _ in range(N)]

for _ in range(M):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = [-1] * N
dist[0] = 0

Q = deque()

Q.append(0)

while len(Q) > 0:
    i = Q.popleft()
    for j in G[i]:
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            Q.append(j)

if dist[N-1] == 2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')



#ヒープを使う
import heapq

N, M = map(int,input().split())

G = [ [] for _ in range(N)]

for _ in range(M):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = [-1] * N

Q = []

heapq.heappush(Q, (0,0))   #（距離、頂点）の順で要素を追加

dist[0] = 0

done = [False] * N 

while len(Q) > 0:
    d, i = heapq.heappop(Q)

    if done[i]:
        continue

    done[i] = True

    for j in G[i]:
        x = 1  #今回は辺の重みは常に0
        if dist[j] == -1 or dist[j] > dist[i] +x:
            dist[j] = dist[i] + x
            heapq.heappush(Q, (dist[j], j))

if dist[N-1] == 2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')