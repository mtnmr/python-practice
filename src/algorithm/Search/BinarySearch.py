#AIZU ALDS1-4-B
#二分探索

def binarySearch(A, key):
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] == key:
            return True
        elif A[mid] > key:
            right = mid
        else:
            left = mid + 1
    return False

n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

cnt = 0
for i in T:
    if binarySearch(S,i):
        cnt += 1

print(cnt)


