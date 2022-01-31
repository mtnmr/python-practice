S = list(input())
revS = list(reversed(S))

if S == revS:
    print('Yes')
    exit()

if revS[0] != 'a':
    print('No')
    exit()

cnt = 0
for s in S:
    if s == 'a':
        cnt += 1
    else:
        break

cnt_a = 0
for x in revS:
    if x == 'a':
        cnt_a += 1
    else:
        break

if (cnt - cnt_a) >= 0:
    print('No')
    exit() 
else:
    S = ['a']*(cnt_a - cnt) + S
    revS = revS + ['a']*(cnt_a - cnt)

    if S == revS:
        print('Yes')
    else:
        print('No')