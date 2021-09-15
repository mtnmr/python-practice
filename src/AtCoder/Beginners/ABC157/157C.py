N, M = map(int,input().split())

num = [''] * N

ok = True

for _ in range(M):
    s, c = map(int,input().split())
    s -= 1
    if num[s] == '':
        num[s] = c
    elif num[s] == c:
        continue
    elif num[s] != c:
        ok = False
        break

for i in range(N):
    if num[i] == '':
        if i == 0 and N != 1:
            num[i] = 1
        else:
            num[i] = 0

if N != 1 and num[0] == 0:
    ok = False

if ok:
    print(''.join(map(str,num)))
else:
    print(-1)