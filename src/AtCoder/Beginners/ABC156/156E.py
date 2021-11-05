#解説みた

n, k = map(int,input().split())

mod = 10**9+7

def cnb(n, x):
    if (x < 0) or (n < x):
        return
    x = min(x, n-x)
    return fact[n] * fact_inv[x] * fact_inv[n-x]

fact = [1, 1] #(n! mod p)を保存
fact_inv = [1, 1] #(n!)**-1 mod p)を保存
inv = [0, 1] #fact_invを計算するために1からNまでの逆元を計算して保存

for i in range(2,n+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    fact_inv.append((fact_inv[-1] * inv[-1]) % mod)

ans = 0
for i in range(min(n-1, k) +1):
    ans += cnb(n, i) * cnb(n-1, n-i-1)
    ans %= mod

#誰もいない部屋の数iを全検索、ただし移動回数kがiの最大
#nCi(空いてる部屋を選ぶ) * n-iHi(重複可でどの部屋に移動するか)　を考える
#xHyは、x+y-1 C x-1 で計算できる

print(ans)