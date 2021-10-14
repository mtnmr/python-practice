L, R = map(int,input().split())

ans = 2018
for i in range(L, R):
    for j in range(L+1, R+1):
        if (i % 2019)==0 or (j % 2019)==0:
            print(0)
            exit()
        else:
            ans = min(ans, (i*j)%2019)

print(ans)