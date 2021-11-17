#AIZU ALDS1-5-C
#コッホ曲線

import math

def koch(n, p1,p2):
    if n == 0:
        return
    
    s_x = (2*p1[0] + 1*p2[0]) / 3
    s_y = (2*p1[1] + 1*p2[1]) / 3
    t_x = (1*p1[0] + 2*p2[0]) / 3
    t_y = (1*p1[1] + 2*p2[1]) / 3
    s = [s_x, s_y]
    t = [t_x, t_y]

    u_x = (t_x-s_x) * math.cos(math.radians(60)) - (t_y-s_y) * math.sin(math.radians(60)) + s_x
    u_y = (t_x-s_x) * math.sin(math.radians(60)) + (t_y-s_y) * math.sin(math.radians(60)) + s_y
    u = [u_x, u_y]

    koch(n-1, p1, s)
    print(*s)
    koch(n-1, s, u)
    print(*u)
    koch(n-1, u, t)
    print(*t)
    koch(n-1, t, p2)

n = int(input())
p1 = [float(0), float(0)]
p2 = [float(100), float(0)]
print(*p1)
koch(n, p1, p2)
print(*p2)