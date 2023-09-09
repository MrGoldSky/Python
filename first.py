f = open("abc.txt", 'r')

s = 0
for i in f:
    z = map(int, i.split())
    a, b, c = map(int, i.split())
    if (max(a, b, c) - min(a, b, c) - sum(z) + max(a, b, c) + min(a,b,c)) > 0:
        s += 1
print(s)