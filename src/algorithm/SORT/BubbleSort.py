#AIZU ALDS1-2-A

def bubbleSort(A, N):
    flag = True
    cnt = 0
    while flag:
        flag = False
        for j in range(N-1, 0, -1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1], A[j]
                cnt += 1
                flag = True
    
    print(*A)
    print(cnt)

N = int(input())
A = list(map(int,input().split()))

bubbleSort(A, N)
                
#提出したコード
def bubbleSort(A,n):
    a = 0
    for i in range(n):
        for j in range(n-1,i,-1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]
                a += 1
    print(*A)
    print(a)