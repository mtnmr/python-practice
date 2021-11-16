#AIZU ALDS1-1-B
#ユーグリット互助法
#整数 x, y について、x ≥ y ならば x と y の最大公約数は y と x % y の最大公約数に等しい。

def gcd(x,y):
    if x < y:
        x,y = y,x
    while y > 0:
        r = x % y
        x = y
        y = r
    return x

x, y = map(int,input().split())

gcd(x,y)