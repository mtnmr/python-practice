n, m = map(int,input().split())

#edgesに頂点iから辺じがある頂点を保存する
edges = [[] for _ in range(n)]

#入次数。始点の判定に使う
indeg = [0] * n

for i in range(m):
    x, y = map(int,input().split())
    edges[x-1].append(y-1)
    indeg[y-1] += 1

#頂点iから始まるパスの最大長
length = [0] * n

#length[i]が既に計算済みかどうかを記録
done = [False] * n

def rec(i):
    if done[i]:
        return length[i]
    else:
        for j in edges[i]:
            length[i] = max(length[i], rec(j)+1)
        done[i] = True
        return length[i]

for i in range(n):
    if indeg[i] == 0:
        rec(i)

print(max(length))