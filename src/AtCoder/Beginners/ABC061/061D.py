def bellman_ford(s):
    dist = [float('inf')] * n
    dist[s] = 0
    for i in range(n):
        update = [False] * n
        for a,b,c in g:
            if  dist[a] + c < dist[b]:
                dist[b] = dist[a] + c
                update[b] = True

        if i == n-1 and update[n-1]:
            return -float('inf')

    return dist[n-1]                

n, m = map(int,input().split())
g = []
for _ in range(m):
    a,b,c = map(int,input().split())
    g.append([a-1, b-1, -c])

ans = bellman_ford(0)
if ans == -float('inf'):
    print('inf') 
else:
    print(-ans)
