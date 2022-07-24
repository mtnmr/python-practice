N  = int(input())
H = list(map(int,input().split()))

cnt = [0] * N

for i in range(N-1):
    if H[i] >= H[i+1]:
        if i == 0:
            cnt[i] = 1
        else:
            cnt[i] = cnt[i-1] + 1

print(max(cnt))