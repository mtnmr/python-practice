N = int(input())
P = list(map(int,input().split()))

cnt = 0

for i in range(N):
    if i+1 == P[i]:
        if i == N-1:
            while P[i] == i+1:
                P[i], P[i-1]  = P[i-1], P[i]
                i -= 1
                cnt += 1

        else:
            P[i], P[i+1] = P[i+1], P[i]
            cnt += 1
    else:
        continue

print(cnt)