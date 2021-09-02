N = int(input())

ans = 0

for A in range(1, N):
    B_count = (N-1) // A
    ans += B_count
    
print(ans)