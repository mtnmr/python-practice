from collections import defaultdict

N = int(input())

dicY = defaultdict(list)
for i in range(N):
    x, y = map(int,input().split())
    dicY[y].append([x, i])
    
S = input()

for y in dicY:
    x_list = dicY[y]
    if len(x_list) == 1:
        continue
    else:
        x_list.sort(key=lambda x: x[0])
        check = False
        for x, i in x_list:
            if S[i] == "R":
                check = True
            if S[i] == "L" and check:
                print("Yes")
                exit()

print("No")