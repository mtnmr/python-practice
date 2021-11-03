N = int(input())

mochi = []
for i in range(N):
    d = int(input())
    mochi.append(d)

mochi_use = set(mochi)

print(len(mochi_use))