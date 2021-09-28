#17566849
h, w, k = map(int,input().split())
MOD = 10 ** 9 + 7

#dp[i][j]上からi行目、左からj番目の縦線にいるパターンの数を記録
dp = [ [0] * w for _ in range(h+1)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        #m:横線の引き方、縦線の数はw-1本、例えばm101なら1-2と3-4に横線あり
        for m in range(1 << (w-1)):
            ok = True
            #横線が連続して引かれているあみだを除外する
            for l in range(w-2):  
                if (m>>l)&1 == 1 and (m>>(l+1))&1 == 1:  #隣り合った２本ともTrueになってるパターン
                    ok = False

            if ok:
                #右へいくパターン
                if j < w-1 and (m>>(w-j-2))&1 == 1:  #jが右端じゃなくてjの右横線(w-2番目までの横線のうちj番目)がTrue
                    dp[i+1][j+1] += dp[i][j]
                    dp[i+1][j+1] %= MOD

                #左へいくパターン
                elif j > 0 and (m>>(w-j-1))&1 == 1:  #jが左端じゃなくてjの左横線(w-2番目までの横線のうちj-1番目)がTrue
                    dp[i+1][j-1] += dp[i][j]
                    dp[i+1][j-1] %= MOD

                #下に降りるパターン
                else:
                    dp[i+1][j] += dp[i][j]
                    dp[i+1][j] %= MOD

print(dp[h][k-1])

#26048314 パターン分けを簡潔にしてある
dp = [ [0] * w for _ in range(h+1)]
dp[0][0] = 1
ALL = 1 << w-1
for i in range(h):
    for j in range(w):
        for bit in range(ALL):
            flg = True
            for k in range(w-2):
                if (bit >> k)&1 and (bit >> (k+1))&1:
                    flg = False
                if not flg:
                    continue

                nw = w
                if (bit >> w) & 1:
                    nw += 1
                elif w > 0 and (bit >> (w-1)) & 1:
                    nw -= 1

                dp[h+1][nw] += dp[h][w]
                dp[h+1][nw] %= dp[h][w]

print(dp[h][k-1])