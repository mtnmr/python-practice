N, K = map(int,input().split())
P = list(map(int,input().split()))

ans_P = []
ans = min(P[:K])
ans_P.append(ans)
for i in range(K, N):
    if P[i] > 
