N, A, B = map(int,input().split())
S = input()

x = A + B

pass_cnt = 0
pass_f = 0

for i, s in enumerate(S):
    if s == 'a':
        if pass_cnt < x:
            print('Yes')
            pass_cnt += 1
        else:
            print('No')
    elif s =='b':
        if (pass_cnt < x) and (pass_f < B):
            print('Yes')
            pass_cnt += 1
            pass_f += 1
        else:
            print('No')
    else:
        print('No')

