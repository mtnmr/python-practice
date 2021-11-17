#AIZU ALDS1-7-A
#根付き木の表現

class Node:
    def __init__(self):
        self.parent_id = -1
        self.depth = 0
        self.type = ''
        self.child = []

n = int(input())

T = []
for _ in range(n):
    t = Node()
    T.append(t)

for _ in range(n):
    u = list(map(int,input().split()))
    id = u[0]
    num = u[1]
    for i in range(num):
        child_id = u[2+i]
        T[child_id].parent_id = id
        T[id].child.append(child_id)

def calc_depth(id, d):
    T[id].depth = d
    for child in T[id].child:
        calc_depth(child, d+1)

for i in range(n):
    if T[i].parent_id == -1:
        calc_depth(i, 0)
        break

for i in range(n):
    if T[i].parent_id == -1:
        T[i].type = 'root'
    elif T[i].child == []:
        T[i].type = 'leaf'
    else:
        T[i].type = 'internal node'

    print(f'node {i}: parent = {T[i].parent_id}, depth = {T[i].depth}, {T[i].type}, {T[i].child}')