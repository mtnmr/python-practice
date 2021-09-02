A, B, C = map(int(input().split()))

#与えられた式を変形すれば計算量が１になる

D = A * (A+1) // 2
E = B * (B+1) // 2
F = C * (C+1) // 2

ans = (D * E * F) % 998244353

print(ans)