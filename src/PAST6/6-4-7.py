import sys
sys.setrecursionlimit(100000)

n = int(input())

#上司bの部下iを記録する
child = [[] for _ in range(n)]
for i in range(1,n):
    b = int(input())
    child[b-1].append(i)

#iの給料を求める再帰関数
def dfs(i):
    if len(child[i]) == 0:
        return 1
    else:
        value = []
        for j in child[i]:
            value.append(dfs(j))
            return max(value) + min(value) + 1

print(dfs(0))