N = int(input())
A = list(map(int,input().split()))

color = [0] * 9
over3200 = 0

for i in range(N):
    a = A[i]
    if 1 <= A[i] < 400:
        color[1] = 1
    elif 400 <= A[i] < 800:
        color[2] = 1
    elif 800 <= A[i] < 1200:
        color[3] = 1
    elif 1200<= A[i] < 1600:
        color[4] = 1
    elif 1600 <= A[i] < 2000:
        color[5] = 1
    elif 2000 <= A[i] < 2400:
        color[6] = 1
    elif 2400 <= A[i] < 2800:
        color[7] = 1
    elif 2800 <= A[i] < 3200:
        color[8] = 1
    elif 3200<= A[i]:
        over3200 += 1

min_color = sum(color)
if min_color == 0:
    min_color = 1

max_color = sum(color) + over3200

print(min_color, max_color)