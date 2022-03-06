N = int(input())

mod = 998244353 

dp = [[0] * 9 for _ in range(N)]
for i in range(9):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(9):
        if j == 0:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j+1]) % mod
        elif j == 8:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % mod

ans = 0
for i in range(9):
    ans += dp[N-1][i]
    ans %= mod

print(ans)

# import sys
# sys.setrecursionlimit(10**9)


# N = int(input())

# ans = 0

# def count(i, cnt):
#     global ans 
#     if cnt == N:
#         ans += 1
#     else:
#         cnt += 1
#         if (i-1) >= 1:
#             count(i-1, cnt)
#         count(i, cnt)
#         if (i+1) <= 9:
#             count(i+1, cnt)

# for i in range(1,10):
#     count(i, 1)

# print(ans %  998244353)