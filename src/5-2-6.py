def is_match(T,S):
    for i in range (0,len(S)-len(t)+1):
        ok = True

        for j in range(0,len(T)):
        if S[i + j] != T[j] and T[j] !=  ".":
            ok = False

        if ok:
            return True
    return False

S = input()

C = "abcdefghijklmnopqrstuvwxyz."

M = []

for T in C:
    if is_match(T,S):
        M.append(T)

for C1 in C:
    for C2 in C:
        T = C1 + C2
        if is_match(T,S):
            M.append(T)

for C1 in C:
    for C2 in C:
        for C3 in C:
            T = C1 + C2 + C3
            if is_match(T,S):
                M.append(T)

print(len(T))
