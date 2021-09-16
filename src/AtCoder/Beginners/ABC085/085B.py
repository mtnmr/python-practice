N = int(input())
D = []
for _ in range(N):
    d = int(input())
    D.append(d)

useD = set(D)
print(len(useD))