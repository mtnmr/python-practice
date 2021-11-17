#AIZU ALDS1-7-B 
#二分木

from typing import Callable


class Node():
    def __init__(self):
        self.parent = -1
        self.sibling = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = ''
        self.left = -1
        self.right = -1

def calc_depth(id, d):
    T[id].depth = d
    if T[id].left != -1:
        calc_depth(T[id].left, d+1)
    if T[id].right != -1:
        calc_depth(T[id].right, d+1)

def calc_height(id):
    h1 = 0
    h2 = 0
    if T[id].left != -1:
        h1 = calc_height(T[id].left) + 1
    if T[id].right != -1:
        h2 = calc_height(T[id].right) + 1
    
    T[id].height = max(h1, h2)
    return T[id].height

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
        T[id].degree += 1

    if right != -1:
        T[right].parent = id
        T[id].degree += 1
    
    if left != -1 and right != -1:
        T[left].sibling = right 
        T[right].sibling = left
    
for i in range(n):
    if T[i].parent == -1:
        calc_depth(i, 0)
        calc_height(i)
        break

for i in range(n):
    if T[i].parent == -1:
        T[i].type = 'root'
    elif T[i].degree == 0:
        T[i].type = 'leaf'
    else:
        T[i].type = 'internal node'

    print(f'node {i}: parent = {T[i].parent}, sibling = {T[i].sibling}, degree = {T[i].degree}, depth = {T[i].depth}, height = {T[i].height}, {T[i].type}')

