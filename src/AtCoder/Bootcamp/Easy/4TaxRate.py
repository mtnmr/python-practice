N = int(input())

a = N // 1.08
b = a + 1

if (int(a*1.08) == N):
    print(int(a))
    exit()
elif (int(b*1.08) == N):
    print(int(b))
    exit()
else:
    print(':(')