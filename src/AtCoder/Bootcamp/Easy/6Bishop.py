H, W = map(int,input().split())

if H == 1 or W == 1:
    ans = 1
elif H % 2 == 0:
    ans = W * (H // 2)
else:
    if W % 2 == 0:
        ans = W * (H // 2) + W//2
    else:
        ans = W * (H // 2) + W//2 + 1

print(ans)
