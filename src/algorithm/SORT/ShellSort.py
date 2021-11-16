#AIZU ALDS1-2-D

def insertionSort(A, n, g):
    global cnt
    for i in range(g,n):
        v = A[i]
        j = i-g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v

def ShellSort(A, n, G):
    m = len(G)
    for i in range(m):
        insertionSort(A, n, G[i])
    
    print(m)

n = int(input())
A = []
for _ in range(n):
    a = input()
    A.append(a)

G = []
g = 1
while g <= n:
    G.append(g)
    g = 3 * g + 1
G.reverse()

cnt = 0

ShellSort(A, n, G)
print(*G)
print(cnt)
for a in A:
    print(a)
