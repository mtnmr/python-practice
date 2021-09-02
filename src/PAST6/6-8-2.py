N = int(input())

BA = []
#開始日Aと終了日Bを[B, A]の順に保存していく(終了日が早い順にBでソートしたいから)

for _ in range(N):
    a, b =map(int,input().split())
    BA.append([b, a])

BA.sort()

ans = 0
last = 0 #終了日を記録

for b, a in BA:
    if last < a:
        ans += 1
        last = b

print(ans)