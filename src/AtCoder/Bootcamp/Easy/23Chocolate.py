N = int(input())
D, X = map(int,input().split())

cnt = 0
for _ in range(N):
    A = int(input())
    cnt += ((D-1)//A +1)

print(cnt+X)