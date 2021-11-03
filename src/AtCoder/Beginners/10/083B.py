N, A, B = map(int,input().split())

total = 0

for i in range(1,N+1):
    str_i = str(i)
    sum_i = 0
    for j in range(len(str_i)):
        sum_i += int(str_i[j])
    if A <= sum_i <= B:
        total += i

print(total)