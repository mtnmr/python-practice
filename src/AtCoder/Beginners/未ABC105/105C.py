N = int(input())

S = []

if N == 0:
    S.append('0')

i = 1
while abs(N) > 0:
    j = 2 ** i
    if N % j == 0:
        S.append('0')
    else:
        S.append('1')
        N -= (-2) ** (i-1)
    i += 1

print(''.join(S[::-1]))