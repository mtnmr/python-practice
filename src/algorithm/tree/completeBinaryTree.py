#AIZU ALDS1-9-A
#完全二分木
#節点の添え字 i が与えられたとき、その親 parent(i)、左の子 left(i)、右の子 right(i) は
# それぞれ ⌊i/2⌋、2×i、2×i+1 で簡単に算出することができる

n = int(input())
H = list(map(int,input().split()))

for i in range(1, n+1):
    print(f'node {i}: key = {H[i-1]}, ', end='')
    if i // 2 >= 1:
        print(f'parent key = {H[i//2-1]}, ', end='')
    if i * 2 <= n:
        print(f'left key = {H[i*2-1]}, ', end='')
    if i*2 +1 <= n:
        print(f'right key = {H[i*2]}, ', end='')
    print()