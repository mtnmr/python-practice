T = int(input())
for _ in range(T):
    a,s = map(int,input().split())
    bit_a = bin(a)
    

# import math

# T = int(input())
# for _ in range(T):
#     a,s = map(int,input().split())
#     for x in range(math.ceil(s/2)+2):
#         if x == math.ceil(s/2)+1:
#             print('No')
#             break

#         y = s - x
#         if (x & y == a):
#             print(x, y)
#             print('Yes')
#             break

#         else:
#             continue