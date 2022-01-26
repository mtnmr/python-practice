import itertools

N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int, input().split()))
L = list(itertools.permutations(range(1,N+1)))

for i, l in enumerate(L):
    if l == P:
        a = i
    if l == Q:
        b = i

print(abs(a-b))

