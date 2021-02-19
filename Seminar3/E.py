s = input()
dic = {}
prev = s[0]
leng = 1
for i in s[1:]:
    if i == prev:
        leng += 1
    else:
        dic.setdefault(prev, 0)
        dic[prev] = max(dic[prev], leng)
        leng = 1
        prev = i
dic.setdefault(prev, 0)
dic[prev] = max(dic[prev], leng)
for c, n in sorted(dic.items()):
    print(c, n)
