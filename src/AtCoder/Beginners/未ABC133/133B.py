N, D = map(int,input().split())
X = []
for _ in range(N):
    x = list(map(int,input().split()))
    X.append(x)

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        dist = 0
        for d in range(D):
            dist += (X[i][d] - X[j][d]) ** 2
        if (int(dist ** 0.5)) ** 2 == dist:
            ans += 1

print(ans)