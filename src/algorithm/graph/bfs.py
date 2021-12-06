#AIZU ALDS1-11-C 
#幅優先検索

from collections import deque

n = int(input())
M = [[] for _ in range(n)]
for _ in range(n):
    u = list(map(int,input().split()))
    i = u[0]-1
    for k in range(u[1]):
        j = u[2+k]-1
        M[i].append(j)

visited = [False] * n
dist = [0] * n

Q = deque()
Q.append(0)
visited[0] = True

while len(Q) > 0:
    u = Q.popleft()
    for v in M[u]:
        if visited[v]:
            continue
        else:
            Q.append(v)
            visited[v] = True
            dist[v] = dist[u] + 1


for i in range(n):
    print(i+1, dist[i])



