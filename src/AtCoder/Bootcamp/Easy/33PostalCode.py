A, B = map(int, input().split())
S = input()

listS = S.split("-")
if len(listS) != 2:
    print("No")
else:
    if len(listS[0]) == A:
        print("Yes")
    else:
        print("No")