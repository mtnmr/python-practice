from collections import defaultdict


N, M = map(int,input().split())
A = list(map(int,input().split()))

A_sum = []
for i in range(N):
    if i == 0:
        A_sum.append(A[i])
    else:
        A_sum.append(A_sum[i-1]+A[i])

cnt = defaultdict(int)
for i in range(N):
    b = A_sum[i] % M
    cnt[b] += 1

ans = 0
ans += cnt[0]
for i in cnt.values():
    ans +=  i * (i-1) // 2

print(ans)
