s = input()
S = list(s)
S.sort()

t = input()
T = list(t)
T.sort(reverse = True)

if S < T:
    print('Yes')
else:
    print('No')
