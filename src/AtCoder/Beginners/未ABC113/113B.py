N = int(input())
T, A = map(int,input().split())
H = list(map(int,input().split()))

temp_lst = []
for i in range(N):
    t = T - H[i] * 0.006
    temp_lst.append(abs(t - A))

min_temp = min(temp_lst)
print(temp_lst.index(min_temp) + 1)

    