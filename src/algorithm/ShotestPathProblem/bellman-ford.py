#Atcoder ABC061D

def bellman_ford(s, n):
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