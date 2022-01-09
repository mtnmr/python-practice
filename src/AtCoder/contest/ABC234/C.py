K = int(input())

ans = [2]

num = 1
i = 0
while num < K:
    i += 1
    num += 2**i

num -= 2**i

cnt = K - num
while i > 0:
    if ((2**i)//2 >= cnt):
        ans.append(0)
    else:
        ans.append(2)
        cnt -= (2**i //2)
    i -= 1

print(int("".join(map(str, ans))))


