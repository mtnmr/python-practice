# S = input()

# ans = 0 
# now = 0
# for i in range(len(S)):
#     if S[i] in ['A', 'C', 'G', 'T']:
#         now += 1
#         ans = max(ans, now)
#     else:
#         now = 0


# print(ans)


S = input()

ans = 0 
for i in range(len(S)):
    if S[i] == 'A' or S[i] =='C' or S[i] =='G' or S[i] == 'T':
        if i == len(S)-1:
            ans = max(ans, 1)
        else:
            for j in range(i+1, len(S)):
                if S[j] != 'A' and S[j] !='C' and S[j] !='G' and S[j] != 'T':
                    break
                else:
                    ans = max(ans, j-i+1)

print(ans)
