N, X = map(int,input().split())
S = input()

T = []
for c in S:
    if c == "U" and len(T) > 0 and (T[-1]=="L" or T[-1]=="R"):
        T.pop()
    else:
        T.append(c)

for c in T:
    if c == "U":
        X //= 2
    elif c == "L":
        X *= 2
    elif c == "R":
        X = 2*X + 1

print(X)


# N, X = map(int,input().split())
# S = input()

# x = X
# for s in S:
#     if s == "U":
#         x //= 2
#     elif s == "L":
#         x *= 2
#     elif s == "R":
#         x = 2*x + 1

# print(x)