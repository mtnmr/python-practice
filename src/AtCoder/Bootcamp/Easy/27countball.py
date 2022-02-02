N, A, B = list(map(int,input().split()))

cnt = N // (A+B)
ans = A * cnt
if N % (A+B) >= A:
    ans += A
else:
    ans += N%(A+B)

print(ans)