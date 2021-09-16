import math

N, H = map(int,input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)

max_A = max(A)
B.sort(reverse=True)
use_B = []
for b in B:
    if b > max_A:
        use_B.append(b)
    else:
        break

cnt = 0
i = 0

while (H > 0) and (i <= (len(use_B) -1)):
    H -= use_B[i]
    cnt += 1
    i += 1

if H > 0:
    cnt += math.ceil(H / max_A)
    
print(cnt)

