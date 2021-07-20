#4-11-1
S = input()

na = S.count('a')
nb = S.count('b')
nc = S.count('c')

if na > nb and na > nc:
    print('a')
elif nb > na and nb > nc:
    print('b')
elif nc > na and nc > nb:
    print('c')

#もっと綺麗
mx = max(na,nb,nc)
if na == mx:
    print('a')
elif nb == mx:
    print('b')
elif nc == mx:
    print('c')

#4-11-2
S = list(map(int,input().split()))
S.sort(reverse =  True)
print(S[2])

#5-1-1
A = []
for _ in range(0,3):
    row = list(map(int,input().split()))
    A.append(row)

M = []
for i in range(0,3):
    row = []
    for j in range(0,3):
        row.append(False)
    M.append(row)

N = int(input())

for _ in range(0,N):
    b = int(input())
    for i in range(0,3):
        for j in range(0,N):
            if A[i][j] == b:
                M[i][j] = True

bingo = False

for i in range(0,3):
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

for i in range(0,3):
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True

if M[0][0] and M[1][1] and M[2][2]:
    bingo = True

if M[0][2] and M[1][1] and M[2][0]:
    bingo = True

if bingo:
    print('Yes')
else:
    print('No')


#5-1-2
C = []
for _ in range(0,3):
    row = list(map(int,input().split()))
    C.append(row)


 ok = True
if C[0][0] - C[0][1] != C[1][0] - C[1][1] or C[1][0] - C[1][1] != C[2][0] - C[2][1]:
    ok = False
if C[0][1] - C[0][2] != C[1][1] - C[1][2] or C[1][1] - C[1][2] != C[2][1] - C[2][2]:
    ok = False
if C[0][0] - C[1][0] != C[0][1] - C[1][1] or C[0][1] - C[1][1] != C[0][2] - C[1][2]:
    ok = False
if C[1][0] - C[2][0] != C[1][1] - C[2][1] or C[1][1] - C[2][1] != C[1][2] - C[2][2]:
    ok = False

if ok:
    print('Yes')
else:
    print('No')

#5-1-3
N = int(input())

S = []
for i in range(0,N):
    si = input()
    si = list(si)
    S.append(si)

for i in range(N-2,-1,-1):
    for j in range(1,2*N-2):
        if S[i][j] == '#':
            if S[i+1][j-1] == 'X':
                S[i][j] == 'X'
            if S[i+1][j] == 'X':
                S[i][j] == 'X'
            if S[i+1][j+1] == 'X':
                S[i][j] == 'X'

for i in range(0,N):
    S[i] = ''.join(S[i])
    print(S[i])


#5-2-2
N = int(input())

z = 0

for i in range(1,555555+1):
    si = str(i)
    ok = True
    
    for s in si:
        if s != si[0]:
            ok = False
        if ok:
            z += 1
        if ok and z == N:
            ans = i
            
print(ans)

#5-2-2
import math
from os import terminal_size
N = int(input())

x = math.ceil(N/9) #keta

y = N % 9  #amari
if y == 0:
    y = 9

ans = ''

for _ in range(0,x):
    ans += str(y)

print(ans)

#5-2-3
K = int(input())
A,B = map(int,input().split())

ok = False

for x in range(A,B+1):
    if x % K == 0:
        ok = True

if ok:
    print('OK')
else:
    print('NG')


#5-2-4
K = int(input())
A,B = map(int,input().split())

ok = False

for i in range(0,10000000):
    if i * K > B:
        break
    if A <= i*K <=B:
        ok = True

if ok:
    print('OK')
else:
    print('NG')

#5-2-6
def is_match(T,S):
    for i in range(0,len(S)-len(T)+1):
        ok = True
        for j in range(0,len(T)):
            if S[i + j] != T[j] and T[j] != ".":
                ok = False
        if ok:
            return True
    return False

S = input()

C = 'abcdefghijklmnopqrstuvwxyz.'
M = []

for T in C:
    if is_match(T,S):
        M.append(T)


for C1 in C:
    for C2 in C:
        T = C1 + C2
        if is_match(T,S):
            M.append(T)

for C1 in C:
    for C2 in C:
        for C3 in C:
            T = C1 + C2 + C3
            if is_match(T,S):
                M.append(T)

print(len(T))

#5-3-1
N,M,Q = map(int,input().split())

graph = []
for i in range(0,N):
    row = []
    for j in range(0,N):
        row.append(False)
    graph.append(row)

for i in range(0,M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    graph[u][v] = True
    graph[v][u] = True

C = list(map(int,input().split()))

for  i in range(0,Q):
    query = list(map(int,input().split()))
   
    if query[0] == 1:
        x = query[1]
        x -= 1
        print(C[x])

        for i in range(0,N):
            if graph[x][i]:
                C[i] = C[x]

    if query[0] == 2:
        x = query[1]
        y = query[2]

        x -= 1
        print(C[x])
        C[x] = y


#5-3-2

for i in range(0,N):
    row = []
    graph.append(row)

for i in range(0,M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

for  i in range(0,Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        x = query[1]
        x -= 1
        for i in graph[x]:
            C[i] = C[x]

    if query[0] == 2:
        x = query[1]
        y = query[2]

        x -= 1

        C[x] = y

#5-3-3
N,Q = map(int,input().split())

graph = []
for i in range(0,N):
    row = []
    for j in range(0,N):
        row.append(False)
    graph.append(row)

for i in range(0,Q):
    query = list(map(int,input().split()))
    a = query[1] - 1

    if query[0] == 1:
        b = query[2] - 1
        graph[a][b] = True
    
    if query[0] == 2:
        for v in range(0,N):
            if graph[v][a]:
                graph[a][v] = True

    if query[0] == 3:
        to_follow = []
        for v in range(0,N):
            if graph[a][v]:
                for w in range(0,N):
                    if graph[v][w] and w != a:
                        to_follow.append(w)

        for w in  to_follow:
            graph[a][w] = True

for i in range(0,N):
    for j in range(0,N):
        if graph[i][j]:
            print('Y',end='')
        else:
            print('N',end = '')

print()


