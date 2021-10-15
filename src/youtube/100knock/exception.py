#０で割った時の例外処理
num = 2
try:
    print(f'計算結果：{10 / num}')
except:
    print('エラー')

#具体的なエラー
num = 2
try:
    print(f'計算結果：{10 / num}')
except ZeroDivisionError as e:
    print(e)

#エラーごとの分岐
def divide(a, b):
    try:
        print(f'計算結果：{a / b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)

#通常終了時に行う処理
def divide(a, b):
    try:
        print(f'計算結果：{a / b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    else:
        print('正常に終了しました')

#全ての処理が終了（例外も含む）
def divide(a, b):
    try:
        print(f'計算結果：{a / b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    finally:
        print('全ての処理が終了しました')

#例外をスルー
def divide(a, b):
    try:
        print(f'計算結果：{a / b}')
    except ZeroDivisionError as e:
        pass
    except TypeError as e:
        pass
    finally:
        print('全ての処理が終了しました')