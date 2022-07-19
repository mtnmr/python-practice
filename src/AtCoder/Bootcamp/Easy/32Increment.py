N = int(input())
S = input()

x = 0
maxX = 0

for s in S:
    if s == "I":
        x += 1
    else:
        x -= 1
    maxX = max(maxX, x)

print(maxX)