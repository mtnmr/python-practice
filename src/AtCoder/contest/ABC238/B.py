N = int(input())
A = list(map(int,input().split()))

cut = [0]
now = 0
for a in A:
    now += a
    if now > 360:
        now -= 360
    cut.append(now)

cut.append(360)
cut.sort()
max_cut = 0
for i in range(N+1):
    max_cut = max(max_cut, cut[i+1]-cut[i])

print(max_cut)