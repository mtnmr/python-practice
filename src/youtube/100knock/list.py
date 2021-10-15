#特定の値抽出
numbers = [0, 3, 8, -4, 9, 1]

print(numbers[1])
print(numbers[-1])
numbers.append(2)

#値を挿入
numbers.insert(0, 5)
numbers.insert(-1, -3)

#値を削除
numbers.remove(5)
numbers.pop(-3)

#フィルター
def isEven(number):
    if number % 2 == 0:
        print(f'This number, {number} is even!')
        return True
    else:
        print(f'This number, {number} is odd!')
        return False

list(filter(isEven, numbers))

#インデックス
numbers.index(-4)

#ソート、昇順降順
numbers.sort()
numbers.sort(reverse = True)