
N = int(input())
A = list(map(int,input().split()))

B = []
for i in range(1, N+1):
    B.append(A[i-1] - i)

B.sort()
b = B[(N // 2)]

sum_A = 0
for i in range(N):
    sum_A += abs(A[i] - b -i -1)

print(sum_A)
