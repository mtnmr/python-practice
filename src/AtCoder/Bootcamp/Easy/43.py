from collections import defaultdict

W = input()
dicW = defaultdict(int)
for w in W:
    dicW[w] += 1

for cnt in dicW.values():
    if cnt % 2 != 0:
        print("No")
        exit()

print("Yes")