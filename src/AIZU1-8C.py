class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def preorder(node):
    if node != None:
        print('', node.key, end='')
        preorder(node.left)
        preorder(node.right)
    
def inorder(node):
    if node != None:
        inorder(node.left)
        print('', node.key, end='')
        inorder(node.right)

root = None

def insert(z):
    global root
    parent = None #xの親を保存する変数
    x = root  #二分木（T）の根
    while x is not None:
        parent = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = parent

    if parent is None:
        root = z
    elif z.key < parent.key:
        parent.left = z
    else:
        parent.right = z

def find(k):
    node = root
    while node != None:
        if node.key == k:
            return node
        elif node.key > k:
            node = node.left
        else:
            node = node.right
    return None

#木の一番左にある数字が最小
def getMinimum(x):
    while x.left != None:
        x = x.left
    return x

#xの次節点を探す
def getSuccessor(x):
    if x.right != None:
        return getMinimum(x.right)
        #xに右分岐があれば、最小値が次節点
    else:
        y = x.parent
        while (y != None) and (x == y.right):
            x = y
            y = y.parent
            #右の分岐がなければ親を辿る。xの次に小さい親を探す
        return y

def deleteNode(z):
    #zに子供がいないか1人だけなら、zを消して子をzの親につなぐ
    #zに子が2人いると、zの次節点（y）をzの代わりに置く。yを消してzを変更。
    if z.left == None or z.right == None:
        y = z
    else:
        y = getSuccessor(z)

    #yの子xを決める。zの次節点yには左分岐は絶対ないから、yの子は必ず1人
    if y.left != None:
        x = y.left
    else:
        x = y.right

    #xの親をyの親に変更
    if x != None:
        x.parent = y.parent

    #yがいた位置にxを入れる
    if y.parent == None:
        root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x

    if y != z:
        z.key = y.key


m = int(input())

for i in range(m):
    order = list(input().split())
    if order[0] == 'insert':
        z = Node(int(order[1]))
        insert(z)
    elif order[0] == 'print':
        inorder(root)
        print()
        preorder(root)
        print()
    elif order[0] == 'find':
        k = int(order[1])
        if find(k):
            print('yes')
        else:
            print('no')
    elif order[0] == 'delete':
        z = find(int(order[1]))
        deleteNode(z)