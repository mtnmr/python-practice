#条件分岐
num = 2
if num > 0:
    print('正の値です')
elif num == 0:
    print('0です')
else:
    print('負の値です')

#複数条件の指定
a = 0
if (0 <= a < 10) and (a % 2 == 0):
    print('一桁の偶数です')
elif (a < 0) and (a % 2 == 1):
    print('負の奇数です')
else:
    print('整数です')