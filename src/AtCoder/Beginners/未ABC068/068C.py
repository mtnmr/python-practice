from collections import deque

N, M = map(int,input().split())

ship = [ [] for _ in range(N)]
for i in range(M):
    a, b = map(int,input().split())
    ship[a-1].append(b-1)
    ship[b-1].append(a-1)

dist = [-1] * N
Q = deque()
Q.append(0)
dist[0] = 0
while len(Q) > 0:
    c = Q.popleft()
    for d in ship[c]:
        if dist[d] == -1:
            dist[d] = dist[c] + 1
            Q.append(d)

if dist[N-1] == 2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')