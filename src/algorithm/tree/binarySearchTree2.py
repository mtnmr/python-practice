#AIZU ALDS1-8-B
#二分探索木find

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


def find(k):
    global root

    node = root
    while node != None:
        if k == node.key:
            return True
        elif k < node.key:
            node = node.left
        else:
            node = node.right
    return False
    

m = int(input())

for _ in range(m):
    order = list(input().split())
    if order[0] == 'insert':
        z = Node(int(order[1]))
        insert(z)
    elif order[0] == 'find':
        k = int(order[1])
        if find(k):
            print('yes')
        else:
            print('no')
    elif order[0] == 'print':
        inorder(root)
        print()
        preorder(root)
        print()