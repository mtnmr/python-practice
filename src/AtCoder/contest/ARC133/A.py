N = int(input())
A = list(map(int,input().split()))

if len(set(A)) == 1:
    print()
    exit()

num = A[0]
for i in range(N-1):
    if A[i] > A[i+1]:
        num = A[i]
        break

    if i == N-2:
        num = A[-1]

for a in A:
    if a != num:
        print(a, '', end='')
print()
