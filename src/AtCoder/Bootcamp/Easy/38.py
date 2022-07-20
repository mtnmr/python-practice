sumTime = 0
dMax = 0
for i in range(5):
    x = int(input())
    cnt = 10 - x%10
    if cnt == 10:
        cnt = 0
    if cnt > dMax:
        dMax = cnt
    sumTime += (x+cnt)

print(sumTime - dMax)
        
    