# TLE
# N = int(input())

# S = input()
# listS = list(S)

# Q = int(input())
# for _ in range(Q):
#     query = input().split()
#     if int(query[0]) == 1:
#         i = int(query[1]) -1
#         c = query[2]
#         listS[i] = c
#     else:
#         l = int(query[1]) -1
#         r = int(query[2]) -1
#         sub_S = listS[l:r+1]
#         print(len(set(sub_S)))


#25813072  木構造を使わずに解決してる例
from bisect import bisect_right, bisect_left
#bisectは、ソートを保ったままxをaに挿入できる点を探す
N = int(input())
S = list(input())
Q = int(input())
Qs = [list(map(str,input().split())) for _ in range(Q)]
alph = {}
for a in [chr(ord('a') + i) for i in range(26)]: 
    alph[a] = []
for i, s in enumerate(S):
    alph[s].append(i)
#アルファベット1文字ずつをキーとして、アルファベットのある位置をメモしていく辞書を作成

for q_type, l, r in Qs:
    if q_type == '1':
        l = int(l) - 1
        ex_alph = S[l]
        if ex_alph == r:
            continue
        
        alph[ex_alph].remove(l)   #もともとl番目にあったalphからlを除く
        b_i = bisect_left(alph[r], l)
        alph[r].insert(b_i, l)
        S[l] = r

    else:
        l, r = int(l)-1, int(r)-1
        tmp = 0
        for key, val in alph.items():   #itemsで辞書型のキーと値に対してループ
            if len(val) == 0:
                continue
            b_a = bisect_left(val, l)
            b_b = bisect_right(val, r)
            if 0 < b_b - b_a:
                tmp += 1   #lとrの間にアルファベットの位置にのindexがあるか

        print(tmp)

