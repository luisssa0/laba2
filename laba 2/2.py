f = 0
a = []
while f == 0:
    c = input()
    if c != 'stop':
        a.append(c)
    else:
        f = 1
print(*a)