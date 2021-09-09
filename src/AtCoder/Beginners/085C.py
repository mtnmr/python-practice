N, Y = map(int,input().split())

ok = False

for a in range(N+1):
    if ok:
        break
    for b in range(N+1 - a):
        c = N - a - b
        price = 10000 * a + 5000 * b + 1000 * c
        if price == Y:
            ok = True
            print(a, b, c)
            break

if ok == False:
    print(-1, -1, -1)