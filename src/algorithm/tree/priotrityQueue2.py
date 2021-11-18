#AIZU ALDS1-9-C
#優先度付きキュー
#heapqライブラリを使う

import heapq

A = []
while True:
    order = list(input().split())
    if order[0] == 'end':
        break
    elif order[0] == 'insert':
        heapq.heappush(A, -int(order[1]))
    elif order[0] == 'extract':
        print(-heapq.heappop(A))

    