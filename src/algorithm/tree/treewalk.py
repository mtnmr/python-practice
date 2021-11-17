#AIZU ALDS1-7-C
#先行巡回(根、左、右)、中間巡回(左、根、右)、後行巡回(左、右、根)

class Node():
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1

def preorder(u):
    print('', u, end='')
    if T[u].left != -1:
        preorder(T[u].left)
    if T[u].right != -1:
        preorder(T[u].right)

def inorder(u):
    if T[u].left != -1:
        inorder(T[u].left)
    print('', u, end='')
    if T[u].right != -1:
        inorder(T[u].right)

def postorder(u):
    if T[u].left != -1:
        postorder(T[u].left)
    if T[u].right != -1:
        postorder(T[u].right)
    print('', u, end='')


n = int(input())

T = []
for _ in range(n):
    t = Node()
    T.append(t)

for _ in range(n):
    u = list(map(int,input().split()))
    id = u[0]
    left = u[1]
    right = u[2]
    T[id].left = left
    T[id].right = right

    if left != -1:
        T[left].parent = id
    if right != -1:
        T[right].parent = id

for i in range(n):
    if T[i].parent == -1:
        root = i
        break

print('Preorder')
preorder(root)
print()
print('Inorder')
inorder(root)
print()
print('Postorder')
postorder(root)
print()