N = int(input())
S = input()
ans_S = list(S)
count = 0

for i in range(N):
    if S[i] == '(':
        count += 1
    else:
        count -= 1
        if count < 0:
            ans_S.insert(0, '(')
            count += 1


if count > 0:
    for i in range(count):
        ans_S.append(')')


print(''.join(ans_S))

