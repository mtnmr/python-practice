N, M = map(int,input().split())

pref = [ [] for _ in range(N)]
city = [ [] for _ in range(M)]
for i in range(M):
    P, Y = map(int,input().split())
    P -= 1
    pref[P].append([Y, i])
    city[i].append(P)

for i in range(N):
    if len(pref[i]) > 0:
        pref[i].sort()
        cnt = 0
        for j in pref[i]:
            cnt += 1
            city[j[1]].append(cnt)

for i in range(M):
    p, x = city[i]
    print('{:0=6}{:0=6}'.format(p+1, x))
