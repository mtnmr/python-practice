from collections import deque

N = int(input())

road = [ [] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    road[a].append(b)
    road[b].append(a)

def bfs(i):
    Q = deque()
    dist = [-1] * N
    dist[i] = 0
    Q.append(i)

    while len(Q) > 0:
        s = Q.popleft()
        for t in road[s]:
            if dist[t] != -1:
                continue
            else:
                dist[t] = dist[s] +1
                Q.append(t)

    return dist

dist_f = bfs(0)
dist_s = bfs(N-1)

Fennec = 0
Snuke = 0

for i, j in zip(dist_f, dist_s):
    if i <= j:
        Fennec += 1
    else:
        Snuke += 1


if Fennec > Snuke:
    print('Fennec')
else:
    print('Snuke')
