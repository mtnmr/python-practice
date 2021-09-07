import bisect

N, M = map(int,input().split())
A = list(map(int,input().split()))

B = [0] * N  #B[k]に子供kが食べた美味しさの最大値の−１倍を保存（bisectは単調増加で使うから）

for a in A:
    k = bisect.bisect_right(B, -a) 
    if k == N:
        print(-1)
    else:
        print(k+1)
        B[k] = -a