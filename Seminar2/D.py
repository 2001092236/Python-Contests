def prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
n = int(input())
i = 2
while n > 0:
    if prime(i):
        n -= 1
    i += 1
print(i - 1)
