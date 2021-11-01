N = int(input())
A = list(map(int,input().split()))

X = [0] * N

S = sum(A)
X[0] += S
for i in range(N):
    if i % 2 == 1:
        X[0] -= A[i] * 2

for i in range(1,N):
    if i == N-1:
        X[i] = 2 * A[i] - X[0]
    else:
        X[i] = 2 * A[i-1] - X[i-1]

print(*X)