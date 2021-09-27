#25874458綺麗

from itertools import accumulate
import bisect

def accumulate_sum(A):
    return list(accumulate(A, initial = 0))

N = int(input())
L = list(map(int,input().split()))

S1 = accumulate_sum(L)
S2 = accumulate_sum(L[::-1])  #逆方向からの累積和を作る

def equal_cut(A, idx):
    med = A[idx] / 2
    _i = bisect.bisect_left(A, med)
    if abs(med - A[_i]) < abs(med - A[_i-1]):
        res = A[_i]
    else:
        res = A[_i-1]

    return [res, A[idx]-res]

ans = float('inf')

for i in range(2, N-1):
    lis = equal_cut(S1, i) + equal_cut(S2, N-i)
    ans = min(ans, max(lis)-min(lis))

print(ans)