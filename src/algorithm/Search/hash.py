#AIZU ALDS1-4-C
#ダブルハッシュを用いたオープンアドレス法
#提出コードはdic[str]=iで辞書型で追加、キーをfindで検索した

#ハッシュ関数は0からm-1(配列のサイズがm)をとるようにするため、例えばh(k) = k mod mにする
mod = 10 ** 9 + 7

def h1(key):
    return key % mod

def h2(key):
    return 1 + (key % (mod-1))

def h(key, i):
    return (h1(key) + i * h2(key)) % mod

def insert(T, key):
    i = 0
    while True:
        j = h(key, i)
        if T[j] == None:
            T[j] = key
            return j
        else:
            i += 1

def search(T, key):
    i = 0
    while True:
        j = h(key, i)
        if T[j] == key:
            return j
        elif T[j] == None or i >= mod:
            return None
        else:
            i += 1

