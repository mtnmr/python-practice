from collections import defaultdict

# N, Q = map(int,input().split())

# A = list(map(int,input().split()))

# dictA = {}
# cntA = {}
# chech = False
# for i, a in enumerate(A):
#     if a not in cntA:
#         cntA[a] = 1
#         dictA[str(a)+str(1)] = i+1
#     else:
#         cntA[a] += 1
#         dictA[str(a)+str(cntA[a])] = i+1 

# for _ in range(Q):
#     x, k = map(int,input().split())
#     q = str(x) + str(k)
#     if q in dictA:
#         print(dictA[q])
#     else:
#         print(-1)

N, Q = map(int,input().split())
A = list(map(int,input().split()))
dicA = defaultdict(list)
for i in range(N):
    dicA[A[i]].append(i+1)

for q in range(Q):
    x, k = map(int,input().split())
   
    if k <= len(dicA[x]):
            print(dicA[x][k-1])
    else:
        print(-1)