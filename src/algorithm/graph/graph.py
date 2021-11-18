#AIZU ALDS1-11-A
#隣接リストから隣接行列を作る

n = int(input())
A = [[0] * n for _ in range(n)]

for _ in range(n):
    u = list(map(int,input().split()))
    i = u[0]-1
    for k in range(u[1]):
        j = u[2+k]-1
        A[i][j] = 1

for i in range(n):
    print(*A[i])