n, L = map(int,input().split())
x = list(map(int,input().split()))
T1, T2, T3 = map(int,input().split())

cost = [float('inf')] * (L+1)
cost[0] = 0

for i in range(1, L+1):
    cost[i] = min(cost[i], cost[i-1]+T1)

    if i >= 2:
        cost[i] = min(cost[i], cost[i-2]+T1+T2) 

    if i >= 4:
        cost[i] = min(cost[i], cost[i-4]+T1+3*T2) 

    if i in x:
        cost[i] += T3

ans = cost[L]
for i in [L-3, L-2, L-1]:
    if i >= 0:
        ans = min(ans, cost[i]+ T1//2 + T2*(2*(L-i)//2)) #式は(L-i-0.5)*T2,答えを整数で出すのに変形

print(ans)