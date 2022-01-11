A, B = map(int,input().split())

cnt = 1
i = 0
while cnt < B:
    i += 1
    cnt += (A-1)

print(i)