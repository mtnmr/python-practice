from collections import deque

N, M, K = map(int,input().split())

friend = [ [] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    friend[a-1].append(b-1)
    friend[b-1].append(a-1)

block = [ [] for _ in range(N)]
for _ in range(K):
    c, d = map(int,input().split())
    block[c-1].append(d-1)
    block[d-1].append(c-1)

ans = [0] * N

reration = [-1] * N
num = 0
size = [0] * N

for i in range(N):
    if reration[i] != -1:
        continue
    else:
        Q = deque()
        Q.append(i)
        reration[i] = num
        size[num] += 1
        while len(Q) > 0:
            j = Q.popleft()
            for k in friend[j]:
                if reration[k] != -1:
                    continue
                else:
                    reration[k] = num
                    size[num] += 1
                    Q.append(k)
        num += 1

for i in range(N):
    ans[i] = size[reration[i]]-1 - len(friend[i])
    for j in block[i]:
        if reration[i] == reration[j]:
            ans[i] -= 1


print(*ans)