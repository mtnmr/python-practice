A, B = map(int, input().split())

ans = 0
for i in range(A, B+1):
    num = str(i)
    reverseNum = num[::-1]
    if num == reverseNum:
        ans += 1

print(ans)