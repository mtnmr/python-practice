N, K = map(int,input().split())

A = list(map(int,input().split()))

#index初期値は数列の両端のすぐ隣にしておく、初期値については条件のチェックをしないから範囲外でも良い
ok = N
ng = -1

#okとngの差が１になったところが境界
while abs(ok-ng) > 1:
    mid = (ok + ng) // 2
    if A[mid] >= K:
        ok = mid
    else:
        ng = mid


if ok == N:
    print(-1)
else:
    print(ok)


#python bisectモジュール
#bisect.bisect_left(A,K) Ai >= Kであるインデックスiのうち最小のものを返す,存在しなければlen(A)
#bisect.bisect_right(A,K) Ai > Kであるインデックスiのうち最小のものを返す

# import bisect

# N, K = map(int,input().split())
# A = list(map(int,input().split()))

# ok = bisect.bisect_left(A,K)

# if ok == N:
#     print(-1)
# else:
#     print(ok)
    

