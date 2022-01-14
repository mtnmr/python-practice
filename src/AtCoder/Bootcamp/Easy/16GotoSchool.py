N = int(input())
A = list(map(int,input().split()))

dict_A = {}
for i, a in enumerate(A):
    dict_A[a] = i+1

for i in range(N):
    print(dict_A[i+1], '', end='')

print()