from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))

dicA = defaultdict(int)
for a in A:
    dicA[a] += 1

for k, v in dicA.items():
    if v == 3:
        print(k)
        exit()
