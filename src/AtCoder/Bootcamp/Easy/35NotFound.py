S = input()
chrs = "abcdefghijklmnopqrstuvwxyz"

setS = set(S)
if len(setS) == 26:
    print("None")
    exit()

for c in chrs:
    if c not in setS:
        print(c)
        exit()