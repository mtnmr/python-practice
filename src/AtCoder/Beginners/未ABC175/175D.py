N, K = map(int,input().split())
P = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = -float('inf')

for i in range(N):
    now = i
    sum_C = []
    while True:
        now = P[now] - 1
        if len(sum_C) == 0:
            sum_C.append(C[now])
        else:
            sum_C.append(C[now]+sum_C[-1])
        
        if now == i:
            break

    l = len(sum_C)
    a = K // l
    b = K % l 
    score = 0
    if sum_C[-1] > 0:
        if  b == 0:
            score = sum_C[-1] * (a-1) + max(sum_C)
        else:
            score = sum_C[-1] * a + max(sum_C[:b])
    else:
        if l > K:
            score = max(sum_C[:K])
        else:
            score = max(sum_C)

    ans = max(ans, score)

print(ans)   

#解説みた,TLE

# N, K = map(int,input().split())
# P = list(map(int,input().split()))
# C = list(map(int,input().split()))

# ans = -float('inf')

# for i in range(N):
#     now = i
#     loop = []
#     num = 0
#     while True:
#         now = P[now] - 1
#         loop.append(C[now])
#         num += C[now]
#         if now == i:
#             break
    

#     l = len(loop)
#     score = 0
#     for j in range(l):
#         score += loop[j]
#         total_score = score
#         if num > 0:
#             cnt = (K - (j+1)) // l
#             total_score += num * cnt

#         ans = max(ans, total_score)

# print(ans)   