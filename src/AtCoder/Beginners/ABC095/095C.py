A, B, C, X, Y = map(int,input().split())

if X >= Y:
    cmax = X * 2
else:
    cmax = Y * 2

min_cost = float('inf')

for c in range(0, cmax+1, 2):
    a = X - c // 2
    b = Y - c // 2
    if a >= 0 and b >= 0:
        cost = A * a + B * b + C * c
    elif a < 0 and b >= 0:
        cost = B * b + C * c  
    elif b < 0 and a >= 0:
        cost = A * a + C * c

    min_cost = min(min_cost, cost)

print(min_cost)