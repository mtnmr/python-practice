A = list(input().split())
stack = []

for a in A:
    if a == '+':
        x = stack.pop()
        y = stack.pop()
        stack.append(y+x)
    elif a == '-':
        x = x = stack.pop()
        y = stack.pop()
        stack.append(y-x)
    elif a == '*':
        x = stack.pop()
        y = stack.pop()
        stack.append(y*x)
    else:
        stack.append(int(a))

print(stack.pop())

