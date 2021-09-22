#解説見た

s = input()
x, y = map(int,input().split())

split_s = s.split('T')
x_cnt = []
y_cnt = []
for i in range(len(split_s)):
    if i % 2 == 0:
        x_cnt.append(int(len(split_s[i])))
    else:
        y_cnt.append(int(len(split_s[i])))

x_position = {0}
for i in range(len(x_cnt)):
    now_x = set()
    if i == 0:
        now_x.add(x_cnt[i])
    else:
        for j in x_position:
            now_x.add(j + x_cnt[i])
            now_x.add(j - x_cnt[i])
    x_position = now_x

y_position = {0}
for i in range(len(y_cnt)):
    now_y = set()
    for j in y_position:
        now_y.add(j + y_cnt[i])
        now_y.add(j - y_cnt[i])
    y_position = now_y

if (x in x_position) and (y in y_position):
    print('Yes')
else:
    print('No')
