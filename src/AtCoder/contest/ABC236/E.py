import numpy as np

N = int(input())
A = list(map(int,input().split()))

meanA = np.mean(np.array(A))
useA = [False] * N
sumA = 0
cnt = 0
for i in range(N):
    if A[i] >= meanA:
        sumA += A[i]
        cnt += 1
        useA[i] = True
    else:
        if i >= 1:
            if not useA[i-1]:
                plusA = max(A[i-1], A[i])
                sumA += plusA
                useA[plusA] = True
                cnt += 1

print(sumA/cnt)

