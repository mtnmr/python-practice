from cmath import inf


S = input()
lenS = len(S)

ans = float('inf')

for i in range(lenS-2):
    X = S[i:i+3]
    ans = min(ans, abs(int(X)-753))

print(ans)
