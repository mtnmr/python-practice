N = int(input())

max_cnt = -1
ans = -1

for i in range(1, N+1):
    num = i
    cnt = 0
    while num % 2 == 0:
        num //= 2
        cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        ans = i

print(ans)