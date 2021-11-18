#AIZU ALDS1-10-B
#連鎖行列積のスカラー乗算の最小回数

n = int(input())
p = []
for i in range(n):
    m = list(map(int,input().split()))
    if i == 0:
        p.append(m[0])
        p.append(m[1])
    else:
        p.append(m[1])

m = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    m[i][i] = 0  #１つの行列を計算するコストは0

for l in range(1, n):  #対象にする行列の数
    for i in range(n-l):
        j = i + l
        #l個の行列を対象に、i番目からj番目の行列積の回数を計算する
        for k in range(i, j):
            m[i][j] = min(m[i][j], m[i][k]+m[k+1][j] + p[i-1]*p[k]*p[j])

print(m[0][n-1])

