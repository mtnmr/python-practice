class SegTree:
  # arr = 配列
  # segfunc = 関数
  # ide_ele = 単位元
  
  def __init__(self,arr,segfunc,ide_ele):
    n = len(arr)
    self.segfunc = segfunc
    self.ide_ele = ide_ele
    #セグ木の深さ
    self.num = 1<<(n-1).bit_length()
    self.tree = [ide_ele]*2*self.num
    for i in range(n):
      self.tree[self.num+i] = arr[i]
    for i in range(self.num-1,0,-1):
      self.tree[i] = self.segfunc(self.tree[2*i],self.tree[2*i+1])
    
  def add(self,k,x):
    k += self.num
    self.tree[k] += x
    while k>1:
      self.tree[k>>1] = self.segfunc(self.tree[k],self.tree[k^1])
      k >>= 1
  
  def xor(self,k,x):
    k += self.num
    self.tree[k] ^= x
    while k>1:
      self.tree[k>>1] = self.segfunc(self.tree[k],self.tree[k^1])
      k >>= 1
    
  def update(self,k,x):
    k += self.num
    self.tree[k] = x
    while k>1:
      self.tree[k>>1] = self.segfunc(self.tree[k],self.tree[k^1])
      k >>= 1
    
  def query(self,l,r):
    res = self.ide_ele
    l += self.num
    r += self.num
    while l<r:
      if l&1:
        res = self.segfunc(res,self.tree[l])
        l += 1
      if r&1:
        res = self.segfunc(res,self.tree[r-1])
      l >>= 1
      r >>= 1
    return res