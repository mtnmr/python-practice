#AIZU ALDS1-5-A 

#全検索
def solve(A, i, m):
    n = len(A)
    if m == 0:
        return True

    elif m < 0:
        return False
    
    elif i >= n:
        return False
    else:
        res = solve(A, i+1, m) or solve(A, i+1, m-A[i])
        return res

n = int(input())
A = list(map(int,input().split()))
q = int(input())
M = list(map(int,input().split()))

for m in M:
    if sum(A) < m:
        print('no')
    elif solve(A, 0, m):
        print('yes')
    else:
        print('no')


#集合を使った回答
n = int(input())
A = list(map(int,input().split()))
q = int(input())
M = list(map(int,input().split()))

flag = [False] * 2000
for i in range(1<<len(A)):
    m = 0
    for j in range(len(A)):
        if 1 & (i>>j) == 1:
            m += A[j]
    flag[m] = True

for m in M:
    print('yes' if flag[m] else 'no')