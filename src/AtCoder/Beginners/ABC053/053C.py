x = int(input())

ans = (x // 11) * 2

y = x % 11
if 1 <= y <= 6:
    ans += 1
elif y > 6:
    ans += 2

print(ans)
