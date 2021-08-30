class Node:
  def __init_(self, key, priority):
    self.key = key
    self.priority = priority
    self.left = None
    self.right = None
    self.parent = None

root = None

def insert(T,z):
  global root
  y = None
  x = root
  while x != None:
    y = x
    if z.key < x.key:
      x = x.left
    else:
      x = x.right

  z.parent = y

  if y == None:
    root = z
  elif z.key < y.key:
    y.left = z
  else:
    y.right = z

  