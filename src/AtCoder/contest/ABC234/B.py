import math

N = int(input())

A = []
for _ in range(N):
    xy = list(map(int,input().split()))
    A.append(xy)

max_len = 0

for x1, y1 in A:
    for x2, y2 in A:
        len = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        max_len = max(max_len, len)

print(max_len)