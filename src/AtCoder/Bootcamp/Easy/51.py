N, A, B = map(int,input().split())

ans = 0
for i in range(1, N+1):
    listI = list(map(int, list(str(i))))
    sumI = sum(listI)
    if A <= sumI <= B:
        ans += i

print(ans)