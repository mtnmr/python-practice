#AIZU ALDS1-2-C ソート後、安定な出力かどうか

#O(n4)
def isstable(A, B):
    for i in range(n):
        for j in range(i+1,n):
            for a in range(n):
                for b in range(a+1,n):
                    if A[i] == A[j] and A[i] == b[b] and A[j] == B[a]:
                        return False
    return True



#bubbleはいつも安定ソートであることを利用
def BubbleSort(C,n):
    for i in range(n):
        for j in range(n-1,i,-1):
            if C[j][1] < C[j-1][1]:
                C[j],C[j-1] = C[j-1],C[j]
    return ' '.join(C)

def SelectionSort(C,n):
    for i in range(n):
        minj = i 
        for j in range(i,n):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i],C[minj] = C[minj],C[i]

n = int(input())
C = list(input().split())
D = C.copy()
A = BubbleSort(C,n)
B = SelectionSort(D,n)

print(A)
print('Stable')
print(B)
if A == B:
    print('Stable')
else:
    print('Not stable')

