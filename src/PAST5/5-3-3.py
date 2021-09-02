N,Q = map(int,input().split())

graph = []
for i in range(0,N):
    row = []
    for j in range (0,N):
        row.append(False)
    graph. append(row)

for i in range(0,Q):
    query = list(map(int,input().split))

    a = query[1]-1

    if query[0] == 1:
        b = query[2]-1
        graph[a][b] = True

    if query[0] == 2:
        for v in range(0,N):
            if graph[v][a]:
                graph[a][v] = True

    if query[0] == 3:
        to_follow = []
        for v in range(0,N):
            if graph[a][v]:
                for w in range(0,N):
                    if graph[v][w] and w != a:
                        to_follow.append(w)

        for w in to_follow:
            graph[a][w] = True

for i in range(0,N):
    if graph[i][j]:
        print('Y',end='')
    else:
        print('N',end='')

print()
