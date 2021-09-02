R, B = map(int,input().split())
x, y = map(int,input().split())

#X個の花束が作れるか判定する関数
#X個の花束を作るにはRとBが１本ずつ固定で必要、残りのRとBで花束を作るセットが何個作れるか考える
def check(X):
    r = R - X
    b = B - X
    if r < 0 or b < 0:
        return False
    else:
        num = (r // (x-1)) + (b // (y-1))
        return (num >= X)

ok = 0
ng = 10 ** 18 + 1

while abs(ng - ok) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)