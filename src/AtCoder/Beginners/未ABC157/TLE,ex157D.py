# from collections import deque

# N, M, K = map(int,input().split())

# friend = [ [] for _ in range(N)]
# for _ in range(M):
#     a, b = map(int,input().split())
#     friend[a-1].append(b-1)
#     friend[b-1].append(a-1)

# block = [ [] for _ in range(N)]
# for _ in range(K):
#     c, d = map(int,input().split())
#     block[c-1].append(d-1)
#     block[d-1].append(c-1)

# ans = [0] * N

# reration = [-1] * N
# num = 0

# for i in range(N):
#     if reration[i] != -1:
#         continue
#     else:
#         Q = deque()
#         Q.append(i)
#         reration[i] = num
#         while len(Q) > 0:
#             j = Q.popleft()
#             for k in friend[j]:
#                 if reration[k] != -1:
#                     continue
#                 else:
#                     reration[k] = num
#                     Q.append(k)
#         num += 1

# for i in range(N-1):
#     for j in range(i+1, N):
#         if (j not in friend[i]) and (j not in block[i]) and (reration[i] == reration[j]):
#             ans[i] += 1
#             ans[j] += 1

# print(*ans)


#親が決まってなければxをそのまま返して、決まっていれば親の番号を返す
def root(x):
    if par[x] < 0:
        return x
    else:
        par[x] = root(par[x])
        return par[x]


def unite(x,y):
    x, y = root(x), root(y)
    if x == y:
        return
    #既に同じ親が入っていたら何もしない

    if par[x] > par[y]:
        x, y = y, x
    #親にはparにもともと入れていた−１が集まってくるため、大元の親になる数字は一番小さい.
    #xを親として以下のコードを考えたいから、逆だったら入れ替える

    par[x] += par[y] #親が決まっていないと初期値−１がpar[x]に足される,別のループの親でも同じ
    par[y] = x

def size(x):
    x = root(x)
    return -par[x]
    #基準にした親には、それにつながる子供が−１ずつ足されている

def same(x, y):
    return root(x) == root(y)

N, M, K = map(int,input().split())
par = [-1] * N
friend = [1] * N #始めから自分の分の１を足しておく

for _ in range(M):
    A, B = map(int,input().split())
    unite(A, B)
    friend[A] += 1
    friend[B] += 1

ans = [None] * N
for i in range(N):
    ans[i] = size(i) - friend[i]

for _ in range(K):
    C, D = map(int,input().split())
    if same(C,D):
        ans[C] -= 1
        ans[D] -= 1

print(*ans)