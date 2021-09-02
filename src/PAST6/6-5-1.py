n = int(input())

A = []
#A[i]はA[i][i+1]から始まる、0-iまではダミーを入れておく。
for i in range(n-1):
    lst = list(map(int,input().split()))
    A.append([0] * (i+1) + lst)

#集合としてあり得るものの個数(0〜2**n-1まで）。左ビットシフト,2**nと同じ意味
ALL = 1<<n

happy = [0] * ALL

#集合nの中に要素ig含まれるか判定してboolianを返す
def has_bit(n, i):
    return (n & (1<<i) > 0)

for n in range(ALL):
    for i in range(n):
        for j in range(i+1, n):
            if has_bit(n,i) and has_bit(n, j):
                happy[n] += A[i][j]


ans = -float('inf')

for n1 in range(ALL):
    for n2 in range(ALL):
        if (n1 & n2) > 0:
            continue
        else:
            n3 = ALL-1 - (n1|n2)
            #n3は、n1とn2の和集合の補集合
            ans = max(ans, happy[n1]+happy[n2]+happy[n3])

print(ans) 