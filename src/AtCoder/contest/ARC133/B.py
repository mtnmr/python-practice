N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

ans = 0

while N > 0:
    cnt = 0
    now = 0
    for p in P:
        for j in range(cnt, N):
            if Q[j] % p == 0:
                now += 1
                cnt = j+1
                print(j)
                break

    ans = max(ans, now)
    P = P[1:]
    N -= 1

print(ans)
