H = int(input())

ans = 1
cnt = 1

while H > 1:
    H //= 2
    cnt *= 2
    ans += cnt

print(ans)