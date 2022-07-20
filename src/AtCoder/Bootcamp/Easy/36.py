N, M = map(int,input().split())

minNum = 0
maxNum = N
for i in range(M):
    L, R = map(int,input().split())
    if L > maxNum or R < minNum:
        print(0)
        exit()
    if L > minNum:
        minNum = L
    if R < maxNum:
        maxNum = R

print(maxNum - minNum + 1)