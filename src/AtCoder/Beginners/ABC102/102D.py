#解説見た

from bisect import bisect_left

N = int(input())
A = list(map(int,input().split()))
sum_A = []
sum_A.append(A[0])
for i in range(1, N):
    sum_A.append(sum_A[i-1] + A[i])


def left_cut(i):
    med = sum_A[i] / 2
    index = bisect_left(sum_A, med)
    if index == 0:
        return [sum_A[index], sum_A[i]-sum_A[index]]
    elif index == i:
        return [sum_A[index-1], sum_A[index]-sum_A[index-1]]
    else:
        #indexを含むか含まないかの２パターンがある
        cut_1 = abs(sum_A[index] - (sum_A[i]-sum_A[index]))
        cut_2 = abs(sum_A[index-1] - (sum_A[i]-sum_A[index-1]))
        if cut_1 < cut_2:
            return [sum_A[index], sum_A[i]-sum_A[index]]
        else:
            return [sum_A[index-1], sum_A[i]-sum_A[index-1]]

def right_cut(i):
    if (sum_A[i+1]-sum_A[i]) > (sum_A[N-1]-sum_A[i+1]):
        return [sum_A[i+1]-sum_A[i], sum_A[N-1]-sum_A[i+1]]
    else:
        ok = i+1
        ng = N-1
        while (ng-ok) > 1:
            m = (ng+ok) // 2
            if (sum_A[m]-sum_A[i]) < (sum_A[N-1]-sum_A[m]):
                ok = m
            else:
                ng = m
            #okとngの間に合計が半分になる点があることがわかる
        cut_1 = abs((sum_A[ok]-sum_A[i]) - (sum_A[N-1]-sum_A[ok]))
        cut_2 = abs((sum_A[ok+1]-sum_A[i]) - (sum_A[N-1]-sum_A[ok+1]))
        if cut_1 < cut_2:
            return [sum_A[ok]-sum_A[i], sum_A[N-1]-sum_A[ok]]
        else:
            return [sum_A[ok+1]-sum_A[i], sum_A[N-1]-sum_A[ok+1]]


ans = float('inf')
for i in range(1, N-2):
    seg = left_cut(i) + right_cut(i)
    ans = min(ans, max(seg)-min(seg))

print(ans)


