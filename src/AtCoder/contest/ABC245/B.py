N = int(input())
A = list(map(int,input().split()))

setA = set(A)
for i in range(2001):
    if i not in setA:
        print(i)
        exit()