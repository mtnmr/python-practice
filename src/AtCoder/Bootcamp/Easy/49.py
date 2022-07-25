H, W = map(int,input().split())

print("#" * (W+2))

for i in range(1, H+1):
    a = input()
    print("#" + a + "#")

print("#" * (W+2))
