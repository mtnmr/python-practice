N, M, C = map(int,input().split())
B = list(map(int,input().split()))

ans = 0
for i in range(N):
    A = list(map(int,input().split()))
    cnt = C
    for a, b in zip(A, B):
        cnt += a*b
    if cnt > 0:
        ans += 1

print(ans)