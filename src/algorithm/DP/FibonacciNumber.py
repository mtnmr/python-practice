#AIZU ALDS1-10-A
#フィボナッチ数列

n = int(input())

F = [1] * 45
for i in range(2,45):
    F[i] = F[i-1] + F[i-2]

print(F[n])


        