V, A, B, C = map(int,input().split())

D = A+B+C
while V >= D:
    V -= D

if V - A < 0:
    print("F")
elif V -A -B < 0:
    print("M")
else:
    print("T")