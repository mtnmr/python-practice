K, N = map(int,input().split())
A = list(map(int,input().split()))

dist_A = []
for i in range(N):
    if i == N-1:
        dist_A.append(K-A[i]+A[0])
    else:
        dist_A.append(A[i+1]- A[i])

print(sum(dist_A) - max(dist_A))