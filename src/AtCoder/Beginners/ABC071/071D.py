N = int(input())
S1 = input()
S2 = input()

mod = 1000000007
ans = 0

i = 0
while i < N:
    if i == 0:
        if S1[i] == S2[i]:
            #縦
            ans = 3
            i += 1
            now = True
        else:
            #横
            ans += 6
            i +=2
            now = False
    else:
        if S1[i] == S2[i]:
            if now:
                #縦⇨縦
                ans *= 2
            else:
                #横⇨縦
                ans *= 1
            i += 1
            now = True

        else:
            if now:
                #縦⇨横
                ans *= 2
            else:
                #横⇨横
                ans *= 3
            i += 2
            now = False

print(ans % mod)
