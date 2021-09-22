# TLE
# N = int(input())
# A = list(map(int,input().split()))
# B = sorted(A.copy())

# ans = 0

# while len(B) > 0:
#     x = B[0]
#     cnt = 1
#     for i in range(1,len(B)):
#         if B[i] == x:
#             cnt += 1
#         else:
#             break
    
#     if x > cnt:
#         ans += cnt
#     elif x < cnt:
#         ans += (cnt - x)

#     B = B[cnt:]
    
# print(ans) 

from collections import Counter

N = int(input())
A = list(map(int,input().split()))
cntA = Counter(A)

ans = 0

for a in cntA:
    if a > cntA[a]:
        ans += cntA[a]
    elif a < cntA[a]:
        ans += (cntA[a] - a)

print(ans)