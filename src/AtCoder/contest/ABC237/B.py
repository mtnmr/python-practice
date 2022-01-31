H, W = map(int,input().split())
A = []
for _ in range(H):
    w = list(map(int,input().split()))
    A.append(w)

for i in range(W):
    for j in range(H):
        print(A[j][i], '', end='')
    print()



# import numpy as np

# H, W = map(int,input().split())
# A = []
# for _ in range(H):
#     w = list(map(int,input().split()))
#     A.append(w)

# B = (np.array(A)).T.tolist()

# for i in range(W):
#     for j in range(H):
#         print(B[i][j], '',  end='')
#     print()