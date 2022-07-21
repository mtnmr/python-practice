from math import fabs


N, M = map(int,input().split())

favorite = [0] * M
for i in range(N):
    listA = list(map(int,input().split()))
    for j in range(1, listA[0]+1):
        num = listA[j]
        favorite[num-1] += 1

ans = 0
for cnt in favorite:
    if cnt == N:
        ans += 1

print(ans)
