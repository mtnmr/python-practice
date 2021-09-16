#だめポイント
#右回りに進むときの距離が保存できてない
#右回りするか、左回りするか
#どこで回る向きを切り替えたら最大になるか

from collections import deque

N, C = map(int,input().split())

sushi = []
sushi.append([0,0])
for i in range(N):
    x, v = map(int,input().split())
    sushi.append([x, v, i])

eat = [False] * (N+1)
visited = [False] * (N+1)

total_cal = 0

Q = deque()
Q.append([0, 0, 0, 0])   #[距離、基準、カロリー、寿司番号]
eat[0] = True
visited[0] = True
now_num = 0

while len(Q) > 0:
    x, start, v, i = Q.popleft()
    if start != now_num:
        x = min(abs(x - now_num), C - x + now_num)
        start = now_num
        Q.append([x, start, v, i])
        continue

    if not eat[i]:
        if (x - v) <= 0:
            eat[i] = True
            total_cal += v
            now_num = x
        else:
            visited[i] = True

    if i < N:
        if  not eat[i+1] and not visited[i]:
            x1, v1, i1 = sushi[i+1]
            Q.append([x1-now_num, now_num, v1, i1])
    if i >= 1:
         if  not eat[i-1] and not visited[i]:
            x2, v2, i2 = sushi[i-1]
            Q.append([now_num-x2, now_num, v2, i2])
    
    if i == 0:
        Q.append([sushi[1][0], 0, sushi[1][1], 1])
        Q.append([sushi[N][0], 0, sushi[N][1], N])


print(total_cal)

