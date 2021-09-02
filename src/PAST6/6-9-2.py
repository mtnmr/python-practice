a, b, x = map(int,input().split())

ok = 0
ng = 10 ** 9 + 1

while abs(ng - ok) > 1:
    mid = (ok + ng) // 2
    cost = a * mid + b * len(str(mid))
    if cost <= x :
        ok = mid
    else:
        ng = mid

print(ok)