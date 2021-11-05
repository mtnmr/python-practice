N, K = map(int,input().split())

cnt = 1
while N // K >= 1:
    N //= K
    cnt += 1

print(cnt)
