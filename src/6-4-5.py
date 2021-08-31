n = int(input())
ps = [0] + list(map(int,input().split()))

P = sum(ps)

#iまでの問題を解いて合計がsになる解き方があるかをboolianで保存
#得点sのパターンは0〜ps全部の合計まで
exist = [[False]*(P+1) for _ in range(n+1)] 
exist[0][0] = True

for i in range(1,n+1):
    for s in range(P+1):
        if exist[i-1][s]:
            exist[i][s] = True
        if exist[i-1][s-ps[i]]:
            exist[i][s] = True

ans = 0
for s in range(P+1):
    if exist[n][s]:
        ans += 1

print(ans)
