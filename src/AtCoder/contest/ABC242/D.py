S = input()
Q = int(input())

def g(s, add):
    #最初の文字（０文字目）はABCABCABC...の周期で変化するため最初から何文字目かを考える
    return chr((ord(s) - ord("A") + add) % 3 + ord("A"))

def f(t, k):
    #S(t)のk文字目を返す関数
    if t == 0:
        #Sは変化していない時
        return S[k]
    if k == 0:
        #Sをt回変化させた時の０文字目、作成した関数gを使う
        return g(S[0], t)
    
    #kが偶数のとき、f(t,k) は f(t−1, k/2) から1進んだ文字
    #kが奇数のとき、f(t,k) は f(t−1, k-1/2) から2進んだ文字
    return g(f(t-1, k//2), k%2+1)

for i in range(Q):
    t, k = map(int,input().split())
    print(f(t,k-1))

