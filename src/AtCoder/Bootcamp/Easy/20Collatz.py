from collections import defaultdict

s = int(input())
d  = defaultdict(int)
cnt = 1
while True:
    if s not in d:
        d[s] += 1
    else:
        print(cnt)
        break
    
    if s % 2 == 0:
        s //= 2
    else:
        s = 3*s + 1

    cnt += 1
        
