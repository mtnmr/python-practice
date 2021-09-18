#解説見た

H, W = map(int,input().split())
N = int(input())
A = list(map(int,input().split()))

C = [ []  for _ in range(H)]

useA = []
for i in range(N):
    a = A[i]
    for _ in range(a):
        useA.append(i+1)

for i in range(H):
    if i % 2 == 0:
        C[i] = useA[i*W:i*W+W]
    else:
        C[i] = useA[i*W:i*W+W][::-1]

for i in range(H):
    print(*C[i])