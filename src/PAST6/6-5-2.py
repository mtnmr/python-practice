n, m = map(int,input().split())

S = [0] 
C = [0]
for i in range(m):
    s,c = input().split()
    s_val = 0  #集合を数字で表す
    for j in range(n):
        if s[j] == 'Y':
            s_val |= 1<<j
    S.append(s_val)
    C.append(int(c))

ALL = 1<<n

cost = [[float('inf')] * ALL for _ in range(m+1)]
#cosy[i][n]　0-iまでのセットの中で、揃った部品がnの時の最小コストを保存する

cost[0][0] = 0

for i in range(1, m+1):
    for n in range(ALL):
        #iを買わない時
        cost[i][n] = min(cost[i][n], cost[i-1][n])
        #iを買うとき部品はn|S[i]になる　cost[i][n|Si]の最小値を更新する
        cost[i][n|S[i]] = min(cost[i][n|S[i]], cost[i-1][n] + C[i])

ans = cost[m][ALL-1]
if ans == float('inf'):
    ans == -1

print(ans)

        