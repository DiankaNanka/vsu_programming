s = input().split()
a = list(map(len, s))
print(s[a.index(max(a))])
a = [s.count(x) for x in set(s)]
print(list(set(s))[a.index(max(a))])
