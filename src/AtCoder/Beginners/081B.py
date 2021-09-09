N = int(input())
A = list(map(int,input().split()))

cnt = 0
even = True

while even:
    for i in range(N):
        if A[i] % 2 != 0:
            even = False
            break
        else:
            A[i] = A[i] // 2
            if i == N-1:
                cnt += 1

print(cnt)