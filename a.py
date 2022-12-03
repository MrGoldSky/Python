import sys

pokyp = {}

a = list(map(str.strip, sys.stdin))

for i in a:
    b = i.split()
    user, p, count = b[0], b[1], int(b[2])
    if pokyp.get(user) == None:
        pokyp[user] = {}
    pokyp[user][p] = pokyp[user].get(p, 0) + count

for i in pokyp:
    pokyp[i] = dict(sorted(pokyp[i].items(), key=lambda item: item[0]))

for i in pokyp.keys():
    print(f"{i}:")
    pk = pokyp[i]
    for j in pk.keys():
        print(f"{j} {pk[j]}")