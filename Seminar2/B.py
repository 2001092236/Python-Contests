def happy(x):
    s1 = 0
    s2 = 0
    for i in range(0, 3):
        s1 += x % 10
        x //= 10
    for i in range(0, 3):
        s2 += x % 10
        x //= 10
    return s1 == s2
n = int(input())
i = 0
while True:
    if n + i < 1e6 and happy(n + i):
        print(n + i)
        break
    if n - i >= 1e5 and happy(n - i):
        print(n - i)
        break
    i += 1
