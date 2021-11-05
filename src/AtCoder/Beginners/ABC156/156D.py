#解説みた

n, a, b = map(int,input().split())

mod = 10**9+7

def count(n,x):
    p = 1
    q = 1
    for i in range(x):
        p = p * (n - i) % mod
        q = q * (i+1) % mod
    return (p * pow(q, mod-2, mod) % mod)  #フェルマーの小定理

ans = pow(2, n, mod) -1
ans -= count(n,a)
ans -= count(n,b)
print(ans%mod)

