N = int(input())
X = list(map(int,input().split()))
max_x = max(X)
min_x = min(X)

ans = float('inf')

for p in range(min_x, max_x+1):
    sum_x = 0
    for i in range(N):
        sum_x += (X[i] - p) ** 2
    ans = min(ans, sum_x)

print(ans)