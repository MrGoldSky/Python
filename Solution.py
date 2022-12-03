import math
from hashlib import sha512

result = sha512()

a = input()

if a[-1].isdigit() is True:
    v = int(a[-1])
    v1 = ord(a[-1]) // 10
    v2 = ord(a[-1]) % 10
    n = len(a)

    x = v ** 2 + math.factorial(v + 2) + ((v1 * v2) >> 1) * n

    a = str(x) + a

if a[0].isalpha() is True:
    a += str(ord(a[0]))

result = sha512(a.encode())
print(result.hexdigest())