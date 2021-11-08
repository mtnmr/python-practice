N = int(input())
A = list(map(int,input().split()))

total = sum(A)
ans = float('inf')

sunuke = A[0]

if N == 2:
    print(abs(A[0]-A[1]))
    exit()

for i in range(1, N-1):
    sunuke += A[i]
    kuma = total - sunuke
    ans = min(ans, abs(sunuke-kuma))

print(ans)