from collections import deque
from string import ascii_lowercase   #英小文字一覧の取得

Q = int(input())

que = deque()

for i in range(Q):
    values = input().split()

    if values[0] == '1':
        c = values[1]
        x = int(values[2])
        que.append([c, x])
    
    else:
        d = int(values[1])
 
        cnt = {}
        for c in ascii_lowercase:
            cnt[c] = 0     #各アルファベットが何文字消されたか、数を辞書型で管理する

        while d > 0 or len(que) > 0:
            c, x = que[0]
            if d >= x:
                d -= x
                cnt[c] += x
                que.popleft()
            else:
                que[0][1] -= d
                cnt[c] += d
                d = 0
        
        ans = 0
        for c in ascii_lowercase:
            ans += cnt[c] ** 2
        
        print(ans)


