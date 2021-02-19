s = input()
n = int(input())
dic = {}
for i in range(n - 1, len(s)):
    sl = s[i - n + 1:i + 1]
    dic.setdefault(sl, 0)
    dic[sl] += 1
print(sorted([x for x, y in dic.items() if y >= 2]))
