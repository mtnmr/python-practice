import math
from fractions import Fraction

N, L, W = map(int,input().split())
A = list(map(int,input().split()))

# A.append(L)

# cnt = 0
# for i in range(N):
#     if i == 0:
#         if A[i] > 0:
#             cnt += math.ceil(A[i] / W)
#     else:
#         if A[i]+W < A[i+1]:
#             cnt += math.ceil((A[i+1]-A[i]-W) / W)

# print(cnt)

cnt = 0
total = 0
for a in A:
    if total < a:
        # num = math.ceil((a-total) / W)
        # num = -(-((a-total) / W)// 1)
        num = math.ceil(Fraction(a-total) / Fraction(W))
        cnt += num
        total = a+W
    else:
        total = a+W

if total < L:
    # num = math.ceil((L-total) / W)
    # num = -(-((L-total) / W) // 1)
    num = math.ceil(Fraction(L-total) / Fraction(W))
    cnt += num

print(int(cnt))