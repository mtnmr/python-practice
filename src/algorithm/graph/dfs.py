#AIZU ALDS1-11-B
#深さ優先探索

#dfsはオーバーフローを起こす可能性があるため上限をあげる
import sys
sys.setrecursionlimit(10000000)

n = int(input())
M = [[] for _ in range(n)]
for _ in range(n):
    u = list(map(int,input().split()))
    i = u[0]-1
    for k in range(u[1]):
        j = u[2+k]-1
        M[i].append(j)

d = [0] * n
f = [0] * n
visited = [False] * n

time = 1

def dfs(i):
    global time
    visited[i] = True
    d[i] = time
    time += 1

    for u in M[i]:
        if visited[u]:
            continue
        else:
            dfs(u)

    f[i] = time
    time += 1

for i in range(n):
    if visited[i]:
        continue
    dfs(i)

for i in range(n):
    print(i+1, d[i], f[i])