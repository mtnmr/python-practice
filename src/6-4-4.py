n, W = map(int,input().split())
ws = [0]
vs = [0]  #indexとiの値が一致するように先頭に0を入れておく
for _ in range(n):
    w, v = map(int,input().split())
    ws.append(w)
    vs.append(v)

#荷物を1〜iまでで選んで重さの合計がwになる時の価値の総和の最大値を保存する
value = [[-float('inf')] * (W+1) for i in range(n+1)] #最大価値の初期値は小さくしておく

value[0][0] = 0

for i in range(n+1):
    for w in range(W+1):
        #iを使わない時
        value[i][w] = max(value[i][w], value[i-1][w])
        #iを使う時
        if w - ws[i] >= 0:
            value[i][w] = max(value[i][w], value[i-1][w-ws[i]] + vs[i])


ans = max(value[n])
print(ans)




