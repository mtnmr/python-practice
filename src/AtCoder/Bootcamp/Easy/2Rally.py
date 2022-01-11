N = int(input())
X = list(map(int,input().split()))

min_sumX = float('inf')
for i in range(min(X), max(X)+1):
    sumX = 0
    for x in X:
        sumX += (x - i) ** 2
    min_sumX = min(min_sumX, sumX)

print(min_sumX)