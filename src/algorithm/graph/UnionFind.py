#AIZU ALDS1-11-D
#union find

class UnionFind:
    def __init__(self, nmax):
        self.size = [1] * nmax
        self.id = [i for i in range(nmax)]
        
    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def unite(self, p, q):
        i, j = self.root(p), self.root(q)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[j] += self.size[j]

    def same(self, p, q):
        return self.root(p) == self.root(q)

n, m = map(int,input().split())
u = UnionFind(n)
for i in range(m):
    s, t = map(int,input().split())
    u.unite(s,t)

q = int(input())
for i in range(q):
    s, t = map(int,input().split())
    print('yes' if u.same(s,t) else 'no')