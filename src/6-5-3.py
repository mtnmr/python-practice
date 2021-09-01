n = int(input())
A = []
for _ in range(n):
    a = list(map(int,input().split()))
    A.append(a)

ALL = 1<<n

cost = [[float('inf')] * n for _ in range(ALL)]
#cost[n][i]訪問した都市がnで、最後にいる都市がiの最小コスト

cost[0][0] = 0

def has_bit(n, i):
    return (n & (1<<i) > 0)

for s in range(ALL):
    for i in range(n):
        for j in range(n):
            if has_bit(s, j) or i == j:
                continue
            else:
                cost[s|(1<<j)][j] = min(cost[s|(1<<j)][j], cost[s][i] + A[i][j])

print(cost[ALL-1][0])