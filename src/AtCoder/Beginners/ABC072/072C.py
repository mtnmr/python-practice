N = int(input())
A = list(map(int,input().split()))

cnt = [0] * 100001
for i in A:
    if i == 0:
        cnt[i] += 1
        cnt[i+1] += 1
    elif i == 100000:
        cnt[i-1] += 1
        cnt[i] += 1
    else:
        cnt[i-1] += 1
        cnt[i] += 1
        cnt[i+1] += 1

print(max(cnt))

# cnt_A = {}
# for i in range(max(A)+1):
#     cnt_A[i] = 0 

# for i in range(N):
#     cnt_A[A[i]] += 1

# ans = -1
# for i in range(max(A)+1):
#     if i == 0:
#         cnt = cnt_A[i] + cnt_A[i+1]
#     elif i == max(A):
#         cnt = cnt_A[i-1] + cnt_A[i]
#     else:
#         cnt = cnt_A[i-1] + cnt_A[i] + cnt_A[i+1]
    
#     ans = max(ans, cnt)

# print(ans)