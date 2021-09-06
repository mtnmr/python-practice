H, W = map(int,input().split())

A = []
for _ in range(H):
    a = input()
    A.append(a)

cnt = [ [0] * W for _ in range(H)]
cnt[0][0] = 1

MOD = 10 ** 9 + 7

for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            continue
        else:
            if i > 0:
                cnt[i][j] += cnt[i-1][j]
            if j > 0:
                cnt[i][j] += cnt[i][j-1]
            cnt[i][j] %= MOD

print(cnt[H-1][W-1])

