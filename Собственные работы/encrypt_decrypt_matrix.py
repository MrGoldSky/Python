def rotate_matrix(matrix):
    # n = len(matrix)
    # new_matrix = []

    # for i in range(n):
    #     n_matrix = []
    #     for j in range(n):
    #         n_matrix.append(0)
    #     new_matrix.append(n_matrix)

    # for i in range(n):
    #     for j in range(n):
    #         new_matrix[j][n - i - 1] = matrix[i][j]    
    # return(new_matrix)
    return tuple(zip(*matrix[::-1]))

def pprint(matrix):
    if matrix is None:
        print("Строка не может быть зашифрованна.")
    else:
        for i in matrix:
            print(i)

def encrypt_matrix(stri, matrix):
    if len(matrix) % len(stri) != 0:
        return None
    word_matrix = []
    for i in range(len(matrix)):
        n_matrix = []
        for j in range(len(matrix)):
            n_matrix.append(0)
        word_matrix.append(n_matrix)

    n = 0
    for _ in range(4):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    word_matrix[i][j] = stri[n]
                    n += 1
        matrix = rotate_matrix(matrix)
    return word_matrix

def decrypt(matrix, word_matrix):
    result = ""
    if word_matrix is None:
        return "Невозьможно дешифровать"
    for _ in range(4):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    result += word_matrix[i][j]
        matrix = rotate_matrix(matrix)
    return result

matrix = [[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
stri = "qwertyuiopasdgh"
pprint(encrypt_matrix(stri, matrix))
print()
print(decrypt(matrix, encrypt_matrix(stri, matrix)))


