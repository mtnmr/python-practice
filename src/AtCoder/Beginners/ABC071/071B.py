import string

S = set(input())

alp = list(string.ascii_lowercase)

for i in alp:
    if i in S:
        continue
    else:
        print(i)
        exit()

print('None')