str1 = list(input())
str2 = list(input())
if len(str1) > len(str2):
    str2 = str2 + [None] * (len(str1) - len(str2))
dic = dict(zip(str1, str2))
print(sorted(list(dic.items())))
