def to(n, p):
    s = ''
    while n > 0:
        s += str(n % p)
        n //= p
    return s[::-1]
n, p = map(int, input().split(' '))
print(to(n, p))
