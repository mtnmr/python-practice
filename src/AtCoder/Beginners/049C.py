import copy

S = input()
s = copy.copy(S)

ok = True

while ok and len(s) > 0:
    if s[:7] == 'dreamer':
        if s[5:10] == 'erase':
            s = s[5:]
        else:
            s = s[7:]

    elif s[:6] == 'eraser':
        s = s[6:]

    elif s[:5] == 'dream' or s[:5] == 'erase':
        s = s[5:]

    else:
        ok = False

if ok:
    print('YES')
else:
    print('NO')
