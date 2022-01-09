t = int(input())

def f(x):
    return x ** 2 + 2 * x + 3

a = f(t) + t
b = f(t)
c = f(f(t))
d = f(a)
print(f(c + d))