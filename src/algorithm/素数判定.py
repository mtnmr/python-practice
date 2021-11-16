#AIZU ALDS1-1-C
#素数判定
#「合成数 x は p≤√x を満たす素因子 pをもつ」という性質を利用する

import math

def isprime(x):
    if x == 2:
        return True
    
    elif x < 2 or x % 2 == 0:
        return False
    
    i = 3
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i += 2

    return True


n = int(input())
ans = 0
for _ in range(n):
    x = int(input())
    if isprime(x):
        ans += 1

print(ans)