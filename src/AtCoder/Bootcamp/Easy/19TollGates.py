N, M, X = map(int,input().split())
A = list(map(int,input().split()))

cost_zero = 0
cost_n = 0
for a in A:
    if a < X:
        cost_zero += 1
    else:
        cost_n += 1

print(min(cost_zero, cost_n))
