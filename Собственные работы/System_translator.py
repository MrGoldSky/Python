def cc(x, c):
    b = 0
    d = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while x != 0:
        b = x % c
        x = x // c
        result = d[b] + result
    # result = result[::-1]
    return result


n = int(input("Введите систему счисления"))
a = int(input("Введите число"))
y = cc(a, n)
print(f"Число {a} в системе счисление {n} = {y}")
z = int(y, n)
print(f"Число {y} в системе счисления 10 = {z}")



