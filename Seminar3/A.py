words = {}
for i in input().split(' '):
    words.setdefault(i, 0)
    words[i] += 1
print(max(words.values()) / sum(words.values()))
