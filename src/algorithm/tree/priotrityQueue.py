#AIZU ALDS1-9-C
#優先度付きキュー
#自分でheapを構築したパターン,時間がかかる

def parent(i):
    return i // 2

def left(i):
    return i * 2

def right(i):
    return i * 2 + 1

def maxheap(A,i):
    l = left(i)
    r = right(i)
    h = len(A)
    if l <= h  and A[l-1] > A[i-1]:
        largest = l
    else:
        largest = i
    
    if r <= h and A[r-1] > A[largest -1]:
        largest = r

    if largest != i:
        A[i-1],A[largest -1] = A[largest -1],A[i-1]
        maxheap(A,largest)

def heapIncreaseKey(A):
    i = len(A) 
    while (i > 1) and (A[parent(i)-1] < A[i-1]):
        A[i-1], A[parent(i)-1] = A[parent(i)-1], A[i-1]
        i = parent(i)

def heapExtraMax(A):
    max = A[0]
    A[0] = A[-1]
    del A[-1]
    maxheap(A, 1)
    return max

A = []
while True:
    order = list(input().split())
    if order[0] == 'end':
        break
    elif order[0] == 'insert':
        A.append(int(order[1]))
        heapIncreaseKey(A)
    elif order[0] == 'extract':
        print(heapExtraMax(A))