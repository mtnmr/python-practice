from collections import defaultdict

N , K = map(int,input().split())

A = defaultdict(int)
for _ in range(N):
    a, b = map(int,input().split())
    A[a] += b

A_sort = sorted(A)

i = 0
while K > 0:
    num = A_sort[i]
    K -= A[num]
    i += 1

print(num)
