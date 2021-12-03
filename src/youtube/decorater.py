import datetime

def print_datetime(f):
    def wrapper():
        print(f'開始:{datetime.datetime.now()}')
        f()
        print(f'終了:{datetime.datetime.now()}')
    return wrapper

@print_datetime
def calc():
    print(3**5)

#func1(func2)  
#中に入れる関数はかっこつけると実行されてしまうため、かっこつけずにオブジェクトとして入れる

#print_datetime(calc)()   
#メイン処理はcalcで、print_datetimeでデコレーションしている
#これを＠で書き換える


#引数がある時は
def print_datetime(f):
    def wrapper(base, height):
        print(f'開始:{datetime.datetime.now()}')
        f(base, height)
        print(f'終了:{datetime.datetime.now()}')
    return wrapper

@print_datetime
def calc(base, height):
    print(base * height)

#print_datetime(calc)(3, 10) これを＠で表している
calc(3,10)

#ただしこれだとcalcの引数に与えたいものが変わったらwrapperの中身も変えないといけない
def print_datetime(f):
    def wrapper(a, b, c):
        print(f'開始:{datetime.datetime.now()}')
        f(a, b, c)
        print(f'終了:{datetime.datetime.now()}')
    return wrapper

@print_datetime
def calc2(a, b, c):
    print(a * b * c)

@print_datetime
def calc2(a, b, c, d):
    print(a * b * c * d)  #これはエラーになる

#可変長引数を設定する、wrapperの引数を変更
def print_datetime(f):
    def wrapper(*args, **kwargs):
        print(f'開始:{datetime.datetime.now()}')
        f(*args, **kwargs)
        print(f'終了:{datetime.datetime.now()}')
    return wrapper

@print_datetime
def calc2(a, b, c):
    print(a * b * c)

