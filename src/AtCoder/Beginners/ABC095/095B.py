N, X = map(int,input().split())
M = []
for _ in range(N):
    m = int(input())
    M.append(m)

minM = min(M)
totalM = sum(M)

num = N + (X-totalM) // minM

print(num)