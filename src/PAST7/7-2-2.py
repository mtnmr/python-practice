import heapq
import math

N, M = map(int,input().split())
xyc_large = []   #大きい塔の座標
for _ in range(N):
    xyc = list(map(int,input().split()))
    xyc_large.append(xyc)

xyc_small = []   #小さい塔の座標
for _ in range(M):
    xyc = list(map(int,input().split()))
    xyc_small.append(xyc)

def has_bit(n, i):
    return ((n & 1<<i) > 0)

#２つの座標を結ぶコストの計算
def calc_edge_cost(xyc1, xyc2):
    x1, y1, c1 = xyc1
    x2, y2, c2 = xyc2
    cost = math.hypot(x1-x2, y1-y2)
    if c1 != c2:
        cost *= 10
    return cost

ans = float('inf')

#小さい塔の中で使うものを集合で全検索し、使う塔を決めてから最小全域木
for b in range(1<<M):
    xyc_use = []
    for xyc in xyc_large:
        xyc_use.append(xyc)  #大きい塔は全部使うから、useに入れておく
    for i in range(M):
        if has_bit(b, i):
            xyc_use.append(xyc_small[i])
    sz = len(xyc_use)

    #useに入れた塔に対して最小全域木を求める
    Q = []
    heapq.heapify(Q)
    used = [False] * sz
    Q.append([0.0, 0])  #[コスト, index]の順に入れる
    res = 0.0

    while len(Q) > 0:
        cost, i = heapq.heappop(Q)
        if not used[i]:
            res += cost
            used[i] = True
            for j in range(sz):
                if not used[j]:
                    cost = calc_edge_cost(xyc_use[i], xyc_use[j])
                    heapq.heappush(Q, [cost, j])

    ans = min(ans, res)

print(ans)
