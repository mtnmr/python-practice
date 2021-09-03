import heapq

N, M = map(int,input().split())

G = [ [] for _ in range(N)]
for _ in range(M):
    u, v, c = map(int,input().split())
    G[u].append((v, c))
    G[v].append((u, c))

marked = [False] * N
mark_count = 0

marked[0] = True
mark_count += 1

Q = []
for (j, c) in G[0]:
    heapq.heappush(Q, (c, j))

sum = 0
while mark_count < N:
    c, i = heapq.heappop(Q)
    if marked[i]:
        continue

    sum += c
    marked[i] = True
    mark_count += 1

    for (j, c) in G[i]:
        if marked[j]:
            continue
        heapq.heappush(Q, (c,j))

print(sum)
