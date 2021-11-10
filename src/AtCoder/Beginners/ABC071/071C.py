from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))

dic_A = defaultdict(int)
for i in A:
    dic_A[i] += 1

x = 0
dic_x = sorted(dic_A.items(),reverse=True)
for num, cnt in dic_x:
    if cnt >= 2:
        x = num
        dic_A[num] -= 2
        break
    else:
        continue

if x == 0:
    print(0)
    exit()

y = 0
dic_y = sorted(dic_A.items(),reverse=True)
for num, cnt in dic_y:
    if cnt >= 2:
        y = num
        break
    else:
        continue

if y == 0:
    print(0)
    exit()

print(x * y)