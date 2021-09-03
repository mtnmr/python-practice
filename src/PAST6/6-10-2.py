import heapq

N, M = map(int,input().split())

G = [ [] for _ in range(N)]

for _ in range(M):
    u, v, c = map(int,input().split())
    G[u].append((v, c))

dist = [-1] * N
dist[0] = 0

done = [False] * N

Q = []
heapq.heappush(Q, (0, 0))

while len(Q) > 0:
    d, i = heapq.heappop(Q)
    
    if done[i]:
        continue   

    done[i] = True

    for (j, c) in G[i]:
        if dist[j] == -1 or dist[j] > d + c:
            dist[j] = d + c
            heapq.heappush(Q, (dist[j], j))

print(dist[N-1])