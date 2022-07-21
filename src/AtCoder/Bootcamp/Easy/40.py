a, b = map(int,input().split())

if a <= 0 and b >= 0:
    print("Zero")
    exit()

if b < 0 and (b - a + 1) % 2 == 1:
    print("Negative")
    exit()

print("Positive")
