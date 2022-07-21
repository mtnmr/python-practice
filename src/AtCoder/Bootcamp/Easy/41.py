N = int(input())
P = list(map(int, input().split()))

minP = float("inf")
ans = 0
for p in P:
    if p <= minP:
        ans += 1
        minP = p

print(ans)