N = int(input())

plan = []
for _ in range(N):
    plan_t, plan_x, plan_y = map(int,input().split())
    plan.append([plan_t, plan_x, plan_y])

ok = True
x_now = 0
y_now = 0
time = 0

for t,x,y in plan:
    x_cost = abs(x - x_now)
    y_cost = abs(y - y_now)
    t -= time
    if (x_cost + y_cost) > t:
        ok = False
        break
    elif (x_cost + y_cost) <= t:
        if (t - (x_cost + y_cost)) % 2 == 0:
            x_now = x
            y_now = y
            time += t

        else:
            ok = False
            break

if ok:
    print('Yes')
else:
    print('No')



