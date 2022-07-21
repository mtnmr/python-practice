N = int(input())

maxA = 0
num = 0
nextA = 0
for i in range(N):
    a = int(input())
    if a > maxA:
        maxA = a
        num = i
        continue
    if a > nextA:
        nextA = a

for i in range(N):
    if i == num:
        print(nextA)
    else:
        print(maxA)