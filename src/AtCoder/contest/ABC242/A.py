A, B, C, X = list(map(int,input().split()))

if X <= A:
    print(1)
elif (A+1) <= X <= B:
    print(C / (B-A))
else:
    print(0)