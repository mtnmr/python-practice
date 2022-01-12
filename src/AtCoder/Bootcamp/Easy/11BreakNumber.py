N = int(input())

max_num = 1
max_cnt = 0
for i in range(1, N+1):
    cnt = 0
    num = i
    while num % 2 == 0:
        num //= 2
        cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
        max_num = i

print(max_num)