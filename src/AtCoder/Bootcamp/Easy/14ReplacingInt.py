N, K = map(int,input().split())

N -= K * (N//K)
print(min(N, abs(N-K)))