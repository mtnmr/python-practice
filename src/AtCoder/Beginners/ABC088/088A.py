N = int(input())
A = int(input())

ok = False

for i in range(A+1):
    if (N - i) % 500 == 0:
        ok = True
        break
    else:
        continue

if ok:
    print('Yes')
else:
    print('No')
