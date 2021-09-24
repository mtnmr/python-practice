#解説見た　

N, C = map(int,(input().split()))
X = [0]
V = [0]
for _ in range(N):
    x, v = map(int,input().split())
    X.append(x)
    V.append(v)

l = [0] * (N+1)      #左回りでiにいる時点でのカロリーと距離の差
l_max = [0] * (N+1)  #左回りでiにいる時点でのカロリーと距離の差の最大値
now_max = 0
for i in range(1, N+1):
    l[i] = l[i-1] + V[i] - (X[i] - X[i-1])
    now_max = max(now_max, l[i])
    l_max[i] = now_max


X_r = [0] 
for i in range(N, 0, -1):
    X_r.append(C-X[i])
V_r = [0] + V[1:][::-1]


r = [0] * (N+1)
r_max = [0] * (N+1)
now_max = 0
for i in range(1, N+1):
    r[i] = r[i-1] + V_r[i] - (X_r[i] - X_r[i-1])
    now_max = max(now_max,r[i])
    r_max[i] = now_max


ans = 0
for i in range(1, N+1):
    ans = max(ans, l_max[i], l[i]- X[i] + r_max[N-i])      #左周りでiまで行った時、iで止まるか、iから右回りするか
    ans = max(ans, r_max[i], r[i] - X_r[i] + l_max[N-i])   #右回り基準

print(ans)
