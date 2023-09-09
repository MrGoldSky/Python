fi = open("input.txt", "r")

n = int(fi.readline())
a = []

for i in fi.readline().split():
    a.append(int(i))

a = sorted(a)

fo = open("output.txt", "w")

for i in a:
    fo.write(str(i) + ' ')