N = int(input())
A = list(map(int,input().split()))

cnt_4 = 0
cnt_even = 0
cnt_odd = 0

for i in range(N):
    if A[i] % 2 == 0:
        cnt_even += 1
        if A[i] % 4 == 0:
            cnt_4 += 1
    else:
        cnt_odd += 1

ok = False

if cnt_even == N:
    ok = True
elif cnt_4 >= cnt_odd:
    ok = True
elif (N - cnt_4*2) == 1:
    ok = True

if ok:
    print('Yes')
else:
    print('No')

