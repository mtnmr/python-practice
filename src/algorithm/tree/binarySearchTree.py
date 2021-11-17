#AIZU ALDS1-8-A
#二分探索木insert

class Node:
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def preorder(u):
    if u != None:
        print('', u.key, end='')
        preorder(u.left)
        preorder(u.right)

def inorder(u):
    if u != None:
        inorder(u.left)
        print('', u.key, end='')
        inorder(u.right)

root = None

def insert(z):
    global root

    parent = None
    x = root

    while x != None:
        parent = x
        if z.key < parent.key:
            x = x.left
        else:
            x = x.right

    z.parent = parent

    if parent == None:
        root = z
    elif z.key < parent.key:
        parent.left = z
    else:
        parent.right = z

m = int(input())

for _ in range(m):
    order = list(input().split())
    if order[0] == 'insert':
        z = Node(int(order[1]))
        insert(z)
    else:
        inorder(root)
        print()
        preorder(root)
        print()