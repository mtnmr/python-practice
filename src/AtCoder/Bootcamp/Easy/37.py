N, K ,Q = map(int,input().split())
pointList = [K-Q] * N
for i in range(Q):
    a = int(input())
    pointList[a-1] = pointList[a-1] + 1

for point in pointList:
    if point > 0:
        print("Yes")
    else:
        print("No")


