N, x = map(int,input().split())
A = list(map(int,input().split()))

A.sort()

ans = 0
i = 0

while i <= N-1:
    if x >= A[i]:
        ans += 1
        x -= A[i]
        i += 1
    else:
        break

if ans == N and (x > 0):
    print(ans-1)
else:
    print(ans)