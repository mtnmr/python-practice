import math

N = int(input())

ans = N-1
max_a = int(math.sqrt(N)) + 1
for a in range(1, max_a+1):
    if N % a == 0:
        ans = min(ans, a + N//a - 2)

print(ans)