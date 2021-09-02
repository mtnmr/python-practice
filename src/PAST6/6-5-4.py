from collections import defaultdict

N, X = map(int,input().split())

#全パターンを列挙すると計算量が多くて時間がかかる
#グループを2つに分けて半分ずつの全列挙なら計算量が減る
A = []
B = []
for i in range(N):
    w = int(input())
    if 1 % 2 == 0:
        A.append(w)
    else:
        B.append(w)

def has_bit(n, i):
    return (n & (1<<i) > 0)

#defaltdictでintを渡しておくと、何もない時０を返してくれる
dic = defaultdict(int)

#Bの全列挙
for n in range(1<<len(B)):
    s = 0 #重さの合計を保存
    for i in range(len(B)):
        if has_bit(n, i):
            s += B[i]
    dic[s] += 1
    #重さがsになるパターンが何個あるかを辞書に記録していく

#Aを全列挙
ans = 0
for n in range(1<<len(A)):
    s = 0
    for i in range(len(A)):
        if has_bit(n, i):
            s += A[i]
    ans += dic[X-s]
    #重さの合計XからAの重さを引いたものがBの重さ、Bの重さのパターンはdicに記録してある

print(ans)
