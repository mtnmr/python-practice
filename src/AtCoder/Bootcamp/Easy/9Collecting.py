N = int(input())
K = int(input())
X = list(map(int,input().split()))

ans = 0
for x in X:
    if abs(K-x) < x:
        ans += abs(K-x) * 2
    else:
        ans += x * 2

print(ans)