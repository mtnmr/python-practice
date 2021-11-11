#AIZU ALDS1-6-C

import copy

def partition(A, p, r):
    x = A[r][1]
    i = p-1
    for j in range(p, r):
        if A[j][1] <= x:
            i = i+1
            A[i],A[j] = A[j], A[i]
    A[i+1],A[r] = A[r], A[i+1]

    return i+1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

n = int(input())
r = n-1
A = []
for _ in range(n):
    a, b = input().split()
    A.append([a, int(b)])

#今回はstableかも判断するため、最初のAを残しておく
B = copy.deepcopy(A)

quickSort(A, 0, r)

for i in range(n-1):
    if A[i][1] == A[i+1][1]:
        if B.index(A[i]) > B.index(A[i+1]):
            print('Not stable')
            break
else:
    print('Stable')

for i in range(n):
    print(*A[i])