import  math

X = int(input())


while True:
    prime = True
    for i in range(2, int(math.sqrt(X))+1):
        if X % i == 0:
            prime = False
            break

    if prime==True:
        print(X)
        exit()

    else:
        X += 1

# import math

# def isprime(x):
#     for i in range(2, int(math.sqrt(x))+1):
#         if x % i == 0:
#             return False

#     return True

# x = int(input())
# while not isprime(x):
#     x += 1

# print(x)