from collections import deque

N, M = map(int,input().split())
H = list(map(int,input().split()))

G = [ [] for _ in range(N)]

for _ in range(N):
    u, v = map(int,input().split())
    h = H[u-1] - H[v-1]
    if h >= 0:
        G[u-1].append((v-1, h))
        G[v-1].append((u-1, -(h*2)))
    else:
        G[u-1].append((v-1, h*2))
        G[v-1].append((u-1, -h))

cost = [-float('inf')] * N
cost[0] = 0

Q =  deque()
def ans(i, Q, G):
    for xc in G[i]:
        xc.append(Q)
