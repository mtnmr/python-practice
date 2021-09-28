s = input()
A = []
for i in range(len(s)):
    if i % 2 == 0:
        A.append(s[i])

print(''.join(A))


#もっと簡単

# s = input()
# print(s[::2])