X, K, D = map(int,input().split())

X = abs(X)

if X // D >= K:
    #X-DKが正だったら負の方向にしか動かない、maxが大きくオーバービットの可能性あるためX-DK>=0を式変形
    X -= D * K
    
else:
    #０をまたぐ直前まで（X/D回）移動したあと、０の間を往復する
    a = X // D  
    K -= a
    X -= a * D
    if K % 2 == 1:
        X = abs(X - D)

print(X)


#maxが大きいからこれではできない
# X, K, D = map(int,input().split())

# for _ in range(K):
#     if X <= 0:
#         X += D
#     else:
#         X -= D

# print(abs)