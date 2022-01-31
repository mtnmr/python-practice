N = int(input())
S = input()
 
ans = [0] * (N+1)
left = 0
right = -1
for i, s in enumerate(S):
    if s == 'L':
        ans[right] = i
        right -= 1
    else:
        ans[left] = i
        left += 1

ans[left] = N

print(*ans)

# ans = [0]
# now = 0
# for i, s in enumerate(S):
#     if s == 'L':
#         ans.insert(now, i+1)
#     else:
#         ans.insert(now+1, i+1)
#         now += 1
 
# print(*ans)