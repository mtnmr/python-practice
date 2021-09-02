N = int(input())
S = input()

sum_w = [0]
#sum_w[i]に0〜i-1番目までのwの人数を保存する
for i in range(N):
    if S[i] == 'W':
        sum_w.append(sum_w[i] + 1)
    else:
        sum_w.append(sum_w[i] + 0)

min_turn = float('inf')

#iをリーダーにした時の左側にいるwの人数と、右側にいるeの人数を計算する
for i in range(N):
    w = sum_w[i]

    #eの人数は、(i+1)〜(N-1)番目までの全部の人数から(i+1)〜(N-1)番目までのwの人数をひく
    e = (N - 1 - i) - (sum_w[N] - sum_w[i+1])

    turn = w + e
    min_turn = min(min_turn, turn)

print(min_turn)