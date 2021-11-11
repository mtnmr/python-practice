#AIZU ALDS1-6-B

def partition(A, p):
    r = len(A) - 1
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i],A[j] = A[j], A[i]
    A[i+1],A[r] = A[r], A[i+1]

    return i+1

N = int(input())
A = list(map(int,input().split()))

i = partition(A, 0)
print(*A[:i], f'[{A[i]}]', *A[i+1:])

