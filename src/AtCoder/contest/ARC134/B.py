from collections import defaultdict

N = int(input())
S = list(input())

dicS = defaultdict(list)
for i, s in enumerate(S):
    dicS[s] += [i]

i = 0
num = N
# chr_list = list('abcdefghijklmnopqrstuvwxyz')
sortS = sorted(S)
for c in sortS:
    if S[i] > c:
        pos = dicS[c][-1]
        if num >= pos:
            for a in range(i, pos):
                if S[a] > c:
                    S[a], S[pos] = S[pos], S[a]
                    num = pos
                    dicS[c] = dicS[c][:-1]
                    break
            i += 1
        else:
            break
    
    elif S[i] == c:
        i += 1
    
    else:
        break

print(''.join(S))
 
# i = 1
# end = N
# while i < end:
#     sortS = sorted(S[i:end])
#     a = sortS[0]
#     if S[i-1] > a:
#         b = dicS[a][-1]
#         S[i-1], S[dicS[a][-1]] = S[dicS[a][-1]], S[i-1]
#         i += 1
#         end = b
#         dicS[a] = dicS[a][:-1]
#     else:
#         i += 1

# print(''.join(S))
