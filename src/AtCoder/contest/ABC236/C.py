from collections import defaultdict

N, M = map(int,input().split())
S = list(input().split())
T = list(input().split())

dicT = defaultdict(int)
for t in T:
    dicT[t] += 1

for s in S:
    if s in dicT:
        print('Yes')
    else:
        print('No')