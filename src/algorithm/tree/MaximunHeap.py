#AIZU ALDS1-9-B
#maxヒープ（部分木の子のkeyは根のkeyよりも小さい）

def left(i):
    return i*2

def right(i):
    return i*2 +1 

def maxheap(A, i, h):
    l = left(i)
    r = right(i)

    if l <= h and A[l-1] > A[i-1]:
        largest = l
    else:
        largest = i

    if r <= h and A[r-1] > A[largest-1]:
        largest = r

    if largest != i:
        A[i-1], A[largest-1] = A[largest-1], A[i-1]
        maxheap(A, largest, h)

def buildMaxHeap(A, h):
    for i in range(h//2, 0, -1):
        maxheap(A, i, h)

h = int(input())
A = list(map(int,input().split()))

buildMaxHeap(A,h)
print(*A)