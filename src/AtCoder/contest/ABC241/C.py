N = int(input())
S = []
for _ in range(N):
    s = input()
    S.append(s)

for i in range(N):
    cntS = [0] * N
    if S[i][0] == "#":
        cntS[0] += 1

    for j in range(1, N):
        if S[i][j] == "#":
            cntS[j] = cntS[j-1] + 1
        else:
            cntS[j] = cntS[j-1]
        
        if j == 5:
            if cntS[j] >= 4:
                print("Yes")
                exit()

        if j >= 6:
            if cntS[j] - cntS[j-6] >= 4:
                print("Yes")
                exit()

for j in range(N):
    cntS = [0] * N
    if S[0][j] == "#":
        cntS[0] += 1

    for i in range(1, N):
        if S[i][j] == "#":
            cntS[i] = cntS[i-1] + 1
        else:
            cntS[i] = cntS[i-1]
        
        if i == 5:
            if cntS[i] >= 4:
                print("Yes")
                exit()

        if i >= 6:
            if cntS[i] - cntS[i-6] >= 4:
                print("Yes")
                exit()


for i in range(N-5):
    cntS_a = [0] * N
    cntS_b = [0] * N
    if S[0][i] == "#":
        cntS_a[0] += 1
    if S[i][0] == "#":
        cntS_b[0] += 1

    for j in range(1, N-i):
        if S[j][j+i] == "#":
            cntS_a[j] = cntS_a[j-1] + 1
        else:
            cntS_a[j] = cntS_a[j-1]
        
        if S[j+i][j] == "#":
            cntS_b[j] = cntS_b[j-1] + 1
        else:
            cntS_b[j] = cntS_b[j-1]
        
        if j == 5:
            if cntS_a[j] >= 4 or cntS_b[j] >= 4:
                print("Yes")
                exit()

        if j >= 6:
            if cntS_a[j] - cntS_a[j-6] >= 4 or cntS_b[j] - cntS_b[j-6] >= 4:
                print("Yes")
                exit()


for i in range(N-5):
    cntS_a = [0] * N
    cntS_b = [0] * N
    if S[0][N-1-i] == "#":
        cntS_a[0] += 1
    if S[i][N-1] == "#":
        cntS_b[0] += 1

    for j in range(1, N-i):
        if S[j][N-1-i-j] == "#":
            cntS_a[j] = cntS_a[j-1] + 1
        else:
            cntS_a[j] = cntS_a[j-1]
        
        if S[i+j][N-1-j] == "#":
            cntS_b[j] = cntS_b[j-1] + 1
        else:
            cntS_b[j] = cntS_b[j-1]
        
        if j == 5:
            if cntS_a[j] >= 4 or cntS_b[j] >= 4:
                print("Yes")
                exit()

        if j >= 6:
            if cntS_a[j] - cntS_a[j-6] >= 4 or cntS_b[j] - cntS_b[j-6] >= 4:
                print("Yes")
                exit()


print("No")
