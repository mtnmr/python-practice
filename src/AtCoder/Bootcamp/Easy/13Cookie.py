A, B ,C = map(int,input().split())

cnt = 0
dic = {}
if A%2 != 0 or B%2 != 0 or C%2 != 0:
    print(0)
    exit()


while True:
    nextA = (B+C)//2
    nextB = (C+A)//2
    nextC = (A+B)//2
    if (nextA,nextB,nextC) in dic.values():
        print(-1)
        exit()
    else:
        cnt += 1
        dic[cnt] = (nextA,nextB,nextC)

    if (nextA%2 == 0) and (nextB%2 == 0) and (nextC%2 == 0):
        A = nextA
        B = nextB
        C = nextC
    else:
        break

print(cnt)