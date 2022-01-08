A = []
for _ in range(3):
    row = list(map(int,input().split()))
    A.append(row)

M = [[False]* 3 for _ in range(3)]

N = int(input())
for _ in range(N):
    number = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == number:
                M[i][j] = True

for i in range(3):
    if M[i][0] and M[i][1] and M[i][2]:
        print('Yes')
        exit()
    if M[0][i] and M[1][i] and M[2][i]:
        print('Yes')
        exit()

if M[0][0] and M[1][1] and M[2][2]:
    print('Yes')
    exit()

if M[0][2] and M[1][1] and M[2][0]:
    print('Yes')
    exit()

print('No')