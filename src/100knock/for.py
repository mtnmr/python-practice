#リストの要素を表示
names = ['John', 'Kevin', 'Louis']
for name in names:
    print(name)

#range
for i in range(10):
    print(i)

#強制終了
for i in range(10):
    if i == 6:
        print('終了！')
        break
    print(i)

#特定の処理を実行
for i in range(10):
    if i == 3:
        continue
    print(i)

#複数リスト　
lasts = ['A', 'B', 'C']
firsts = ['a', 'b', 'c']
for last, first in zip(lasts, firsts):
    print(last+first)

#要素とインデックスを取得
for i, last in enumerate(lasts):
    print(f'{i}番目の{last}です')

#内包表記
nums = []
for i in range(5):
        nums.append(2 * i)

nums = [2 * i for i in range(5)]