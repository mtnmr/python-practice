N = input()
lenN = len(N)
n = int(N)

ans = 0

if lenN == 1:
    ans = (n * (n+1)) // 2
    print(ans)
    exit()

for i in range(lenN-1):
    a = 9*(10**i)
    ans += (a * (a+1)) // 2

b = 0
for j in range(lenN-1):
    b += 9 * (10**j)

ans += ((n-b) * (n-b+1)) // 2


print(ans % 998244353)

