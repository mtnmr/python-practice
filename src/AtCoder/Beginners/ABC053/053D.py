N = int(input())
A = list(map(int,input().split()))

B = set(A)
num = N - len(B)

ans = len(B)
if num % 2 == 1:
    ans -= 1

print(ans)