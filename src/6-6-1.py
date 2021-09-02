A, R, N = map(int(input().split()))

def solve(A, R, N):
    #R=1の時、n-1乗のループが途中で止まらず実行されるため計算量が大きくなる
    if R == 1:
        return A

    #R>=2の時、Rがどんな値でも30ループ以内に10**9を超える
    for _ in range(N-1):
        A *= R
        if A > 10 ** 9:
            return 'lerge'

    return A

ans = solve(A, R, N)
print(ans)
