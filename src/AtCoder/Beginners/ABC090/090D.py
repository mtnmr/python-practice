N, K =map(int,input().split())

cnt = 0

if K == 0:
    print(N * N)
    exit()

for b in range(1, N+1):
    #N=pb+rの形で考える
    p = N // b
    r = N % b

    #aが0-Nまでの範囲で考えてbで割った余りを並べると、0,1,,,b-1をp回繰り返したのち0,1,,rまでで終わる
    #0,1,,,b-1の中にはk以上を満たすものが(b-1)-k+1個、0,1,,,rにはr-K+1個ある
    #K以上を満たすものがない時は負になってしまうため、max(0,)にする
    a = p * max(0, b-K) + max(0, r-K+1)
    cnt += a

print(cnt)