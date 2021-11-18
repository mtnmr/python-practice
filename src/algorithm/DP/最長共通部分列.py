#AIZU ALDS1-10-C 
#XとYの最長共通部分列longest common subsequenceを動的計画法で求める

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    X = ' ' + X
    Y = ' ' + Y

    max_lcs = 0
    c = [ [0] * (n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] +1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])

            max_lcs = max(max_lcs, c[i][j])

    return max_lcs
            

n = int(input())
for i in range(n):
  X = input()
  Y = input()
  print(lcs(X, Y))


#提出したコード
def lcs(X, Y):
  m = len(X)
  n = len(Y)
  dp = [0] * (n+1)
  for i in range(m):
    memo = dp[:]
    for j in range(n):
      if X[i] == Y[j]:
        dp[j+1] = memo[j] + 1
      elif dp[j+1] < dp[j]:
        dp[j+1] = dp[j]
  return dp[n]

n = int(input())
for i in range(n):
  X = input()
  Y = input()
  print(lcs(X, Y))