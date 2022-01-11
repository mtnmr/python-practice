import math

a, b = input().split()
num = a + b
if math.sqrt(int(num)).is_integer():
    print('Yes')
else:
    print('No')
