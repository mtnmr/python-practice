#AIZU ALDS1-3-B 

from collections import deque

n, q = map(int,input().split())

Q = deque()

for _ in range(n):
    name, time = input().split()
    Q.append([name, int(time)])

now_time = 0
while len(Q) > 0:
    name, time = Q.popleft()
    if time <= q:
        now_time += time
        print(name, now_time)
    else:
        now_time += q
        time -= q
        Q.append([name, time])

