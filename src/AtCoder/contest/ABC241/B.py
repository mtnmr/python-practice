from collections import defaultdict

N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dicA = defaultdict(int)
for a in A:
    dicA[a] += 1

for b in B:
    if dicA[b] > 0:
        dicA[b] -= 1
    else:
        print("No")
        exit()

print("Yes")