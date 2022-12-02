alphabit = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'


def encrypt_caesar(msg, shift, per=1):
    total = ''
    for i in msg:
        if i in alphabit:
            first = alphabit.find(i)
            key = first + shift if per == 1 else first - shift
            if key > len(alphabit):
                key = key % 64
            elif key < 0:
                key = key % 64
            total += alphabit[key]
        else:
            total += i
    return total


def decrypt_caesar(msg, shift):
    return encrypt_caesar(msg, shift, 0)



msg = "Да здравствует салат Цезарь!"
shift = 5
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)