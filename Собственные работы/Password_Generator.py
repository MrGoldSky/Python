from random import choice, shuffle

letter = "qwertyuipasdfghjkzxcvbnmQWERTYUPASDFGHJKLZXCVBNM"
numbers = "23456789"


def generate_password(m):
    let = []
    n = []
    for _ in range(m):
        let.append(choice(letter))
    for _ in range(m):
        n.append(choice(numbers))
    for i in range(len(n)):
        n[i] = str(n[i])
    pas = let + n
    shuffle(pas)
    pas = pas[:m]
    pas = set(pas)
    pas = list(pas)
    pas = "".join(pas)
    return(pas)


def main(n, m):
    a = []
    for _ in range(n):
        b = generate_password(m)
        while b in a:
            b = generate_password(m)
        else:
            a.append(b)
    return(a)


print("Случайный пароль из 20 символов:", generate_password(20))  
