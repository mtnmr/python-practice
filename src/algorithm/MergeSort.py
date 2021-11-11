#AIZU ALDS1-5-B

def merge(A, left, mid, right):
    global cnt
    L = A[left:mid] + [float('inf')]
    R = A[mid:right] + [float('inf')]
    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        cnt += 1

def mergeSort(A, left, right):
    if left+1 < right:
        mid = (left+right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

N = int(input())
A = list(map(int,input().split()))

cnt = 0

mergeSort(A, 0, N)

print(*A)
print(cnt)