N = int(input())
A = []
for _ in range(2*N-1):
    a = list(map(int,input().split()))
    A.append(a)

ans = -float('inf')
use = [False] * (2*N)

def dfs(i, total):
    global ans
    if i == N:
        ans = max(ans, total)
        return 

    for j in range(2*N):
        if not use[j]:
            use[j] = True
            break

    for k in range(j+1, 2*N):
        if not use[k]:
            use[k] = True
            dfs(i+1, total ^ A[j][k-j-1])
            use[k] = False
    use[j] = False 

dfs(0, 0)
print(ans)   
        
