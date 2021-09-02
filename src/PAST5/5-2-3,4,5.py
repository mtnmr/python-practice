K = int(input())

A,B = map(int.input().split())

ok = False

for x in range(A,B+1):
    if x %  K == 0:
        ok = True

if ok:
    print("OK")
else:
    print("NG")





K = int(input())
A,B = map(int.input().split())

ok = False

for i in range(0,1000+1):
    if i * K > B:
        break
    if A <= i * K <= B:
        ok = True

if ok:
    print("OK")
else:
    print("NG")




K = int(input())
A,B = map(int.input().split())

ok = False

x = A // K
u = B // K

if x < u:
    ok = True

# x=uの可能性を考える
if A % K == 0:
    ok = True

if ok:
    print("OK")
else:
    print("NG")