from collections import deque

H, W = map(int,input().split())
S = []
for i in range(H):
    s = input()
    S.append(s)

dist = [[-1] * W for _ in range(H)]

Q = deque()
Q.append([0,0])
dist[0][0] = 1

while len(Q) > 0:
    i, j = Q.popleft()
    for i2, j2 in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
        if not (0 <= i2 < H and 0 <= j2 < W):
            continue
        if S[i2][j2] == '#':
            continue
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])


white_num = 0
for a in range(H):
    for b in range(W):
        if S[a][b] == '.':
            white_num += 1


if dist[H-1][W-1] == -1:
    print(-1)
else:
    ans = white_num - dist[H-1][W-1]
    print(ans)
