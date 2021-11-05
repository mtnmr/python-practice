#invの作りかたが違う例

#1人目

MOD = 1000000007
 
n, k = map(int, input().split())
 
def factorial(n):
    fact = [1] * (n + 1)
    ifact = [0] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i % MOD
    ifact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        ifact[i-1] = ifact[i] * i % MOD
    return fact, ifact
 
fact, ifact = factorial(n * 2)
def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * ifact[r] * ifact[n-r] % MOD
 
ans = 0
for i in range(min(n - 1, k) + 1):
    ans = (ans + comb(n, i) * comb(min(k, i) + n - i - 1, n - i - 1) % MOD) % MOD
print(ans)


#2人目

n, k = map(int, input().split())
mod = 10**9+7
 
fact = [1]
fact_inv = [1]
for i in range(1, 10**5*2+1):
    fact.append(fact[-1]*i%mod)
    fact_inv.append(pow(fact[-1], mod-2, mod))
 
def comb(a, b):
    return fact[a]*fact_inv[b]*fact_inv[a-b]%mod
 
ans = 0
 
for i in range(min(n-1, k)+1):
    ans += comb(n, i) * comb(n-1, n-i-1)
    ans %= mod
 
print(ans)
