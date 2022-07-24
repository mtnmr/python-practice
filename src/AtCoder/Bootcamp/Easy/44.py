S = input()
n = len(S)

cntA = 0  #1010101...
cntB = 0  #0101010...
for i in range(n):
    if i % 2 == 0:
        if S[i] == "0":
            cntA += 1
        else:
            cntB += 1

    else:
        if S[i] == "1":
            cntA += 1
        else:
            cntB += 1

print(min(cntA, cntB))