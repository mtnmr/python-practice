N = int(input())

ok = False
for a in range(N//4 + 1):
    for b in range(N//7 + 1):
        if N - (4*a + 7*b) == 0:
            print('Yes')
            exit()

print('No')