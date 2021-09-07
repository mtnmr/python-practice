N = int(input())

S = ' ' + input()
C = [0] + list(map(int,input().split()))
D = [0] + list(map(int,input().split()))

#cost[i][j] i文字目までの扱いを決めて累積和がjである時の最小コスト
cost = [ [float('inf')] * (N+1) for _ in range(N+1)]

cost[0][0] = 0

for i in range(1,N+1):
    for j in range(i):
        if S == '(':
            #そのまま使う
            cost[i][j+1] = min(cost[i][j+1], cost[i-1][j])
            #反転させる
            if j > 0:
                cost[i][j-1] = min(cost[i][j-1], cost[i-1][j] + C[j])

        else:
            if j > 0:
                cost[i][j-1] = min(cost[i][j-1], cost[i-1][j])
            cost[i][j+1] = min (cost[i][j+1], cost[i-1][j] + C[j])
        #削除する
        cost[i][j] = min(cost[i][j], cost[i-1][j] + D[j])

print(cost[N][0])
