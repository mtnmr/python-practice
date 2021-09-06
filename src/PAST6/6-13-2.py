import sys
sys.setrecursionlimit(1000000)

N = int(input())
R = -1   #社長の番号を記録する、-1にしておいて社長がわかったら更新

edges = [ [] for _ in range(N)]  #edges[i]にiの部下の番号を保存
for i in range(N):
    p = int(input())  #iの親がpとして与えられる
    if p == -1:
        R = i
    else:
        edges[p-1].append(i)

#queries[a]に、[クエリ番号q、bの値]を保存しておいて、bはaの上司かを考えていく。
#ans[q]に「bはaの上司か」をbooleanで記録する。
queries = [ [] for _ in range(N)]
Q = int(input())
for q in range(Q):
    a, b = map(int,input().split())
    queries[a-1].append([q, b-1])

ans = [False] * Q  #クエリの数だけ答えを用意

boss = [False] * N  #頂点iが今見ている頂点の上司か

def dfs(i):
    for q, b in queries[i]:
        ans[q] = boss[b]  #bがaの上司であれば、bossにtrueが入っているはず
    
    boss[i] = True   #この後再帰で自分の部下について考えていくため、自分を上司に設定しておく
    for j in edges[i]:
        dfs(j)    #再帰を考える時点で、jの上司は全てtrueになっている状態
    
    boss[i] = False  #再帰から抜ける時に自分は上司から外す


dfs(R)  #社長から順に再帰を考える

for q in range(Q):
    if ans[q]:
        print('Yes')
    else:
        print('No')

