#AIZU ALDS1-4-A
#番兵法

n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

def linearSearch(key, A, n):
    A[n] = key
    i = 0 
    while A[i] != key:
        i += 1
    if i == n:
        return False
    return True

cnt = 0
S.append(float('inf'))
for key in T:
    if linearSearch(key, S, n):
        cnt += 1

print(cnt)



#提出

n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

C = 0
for i in T:
    if i in S:
        C += 1

print(C)