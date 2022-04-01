N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

useA = [False] * N
useB = [False] * N

useA[0] = True
useB[0] = True

for i in range(N-1):
    if useA[i]:
        if abs(A[i]-A[i+1]) <= K:
            useA[i+1] = True
        if abs(A[i]-B[i+1]) <= K:
            useB[i+1] = True

    if useB[i]:
        if abs(B[i]-A[i+1]) <= K:
            useA[i+1] = True
        if abs(B[i]-B[i+1]) <= K:
            useB[i+1] = True
    
    if useA[i+1] or useB[i+1]:
        continue
    else:
        print("No")
        exit()

print("Yes")