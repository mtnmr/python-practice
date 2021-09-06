N = int(input())
Q = int(input())

row_num = list(range(0,N))
col_num = list(range(0,N))

#転置が起こった時計算式のiとjを逆にする、今の状態を記録。Falseならそのまま、trueは逆。
trans_flag = False

for q in range(Q):
    query = list(map(int,input().split()))
    t = query[0]
    if t != 3:
        A, B = query[1:3] 
        A -= 1
        B -= 1

    if t == 1:
        row_num[A], row_num[B] = row_num[B], row_num[A]
    elif t == 2:
        col_num[A], col_num[B] = col_num[B], col_num[A]
    elif t == 3:
        row_num, col_num = col_num, row_num
        trans_flag = not trans_flag
    elif t == 4:
        if trans_flag:
            print(col_num[B]*N + row_num[A])
        else:
            print(row_num[A]*N + col_num[B])