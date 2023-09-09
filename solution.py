n = int(input())
a = ''

while n > 0:
    a = str(n % 3) + a 
    n = n // 3

while (a.count('0') != 0):
    a = a.replace('10', '03')
    a = a.replace('20', '13')
    a = a.replace('30', '23')
    if a[0] == '0':
        a = a[1:]
print(a)
