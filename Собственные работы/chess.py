WHITE = 1
BLACK = 2
flag00 = False
flag01 = False
flag70 = False
flag71 = False

# Удобная функция для вычисления цвета противника


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE

# Вывод доски


def print_board(board):  # Распечатать доску в текстовом виде (см. скриншот)
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()

# Вывод доски


def main():
    # Создаём шахматную доску
    board = Board()
    # Цикл ввода команд игроков
    while True:
        # Выводим положение фигур на доске
        print_board(board)
        # Подсказка по командам
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <row1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        print("    castling0 и castling7              -- рокировка на col0 или col7")
        # Выводим приглашение игроку нужного цвета
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход чёрных:')
        command = input()
        if command == 'exit':
            break
#!
        # if command == "castling0":
        #     try:
        #         board.castling0()
        #     except False:
        #             print("Рокировка не возможна, введите другую команду")
        #             command = input()
            # else:
            #     print("Выполнена рокировка")
        if command == "castling7":
            try:
                board.castling7()
            except False:
                    print("Рокировка не возможна, введите другую команду")
                    command = input()
            else:
                print("Выполнена рокировка")
        try:
            move_type, row, col, row1, col1 = command.split()
        except TypeError:
            print("Неверный ход")
            command = input()
            move_type, row, col, row1, col1 = command.split()
        except ValueError:
            print("Неверный ход")
            command = input()
            move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Ход успешен')
        else:
            print('Координаты некорректы! Попробуйте другой ход!')

# Функция проверяет, что координаты (row, col) лежат внутри доски


def correct_coords(row, col):
    '''Функция проверяет, что координаты (row, col) лежат
    внутри доски'''
    return 0 <= row < 8 and 0 <= col < 8


class Board:

    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), None, None, None,
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        # self.field[1] = [
            # Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            # Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        # ]
        # self.field[6] = [
            # Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            # Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        # ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]


        # self.field[0] = [
            # Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            # King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        # ]
        # self.field[1] = [
        #     Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
        #     Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        # ]
        # self.field[6] = [
        #     Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
        #     Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        # ]
        # self.field[7] = [
            # Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            # King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        # ]
# Возврат цвета игрока

    def current_player_color(self):
        return self.color

# Проверка пуста ли клетка (Для вывода доски)

    def cell(self, row, col):
        '''Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела.'''
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

# Возврат координат фигуры

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None

# Передвижение фигуры

    def move_piece(self, row, col, row1, col1):
        '''Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False'''

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False
        else:
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)
        return True

# Преобразование пешки

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        if not isinstance(self.field[row][col], Pawn):
            return False
        if self.field[row1][col1] is not None:
            if not self.field[row][col].can_attack(self, row, col, row1, col1):
                return False
        else:
            if not self.field[row][col].can_move(self, row, col, row1, col1):
                return False
        p = self.field[row][col]
        if char == 'Q':
            self.field[row1][col1] = Queen(p.get_color())
            self.field[row][col] = None
        elif char == 'R':
            self.field[row1][col1] = Rook(p.get_color())
            self.field[row][col] = None
        elif char == 'B':
            self.field[row1][col1] = Bishop(p.get_color())
            self.field[row][col] = None
        elif char == 'N':
            self.field[row1][col1] = Knight(p.get_color())
            self.field[row][col] = None
        self.color = opponent(self.color)
        return True

# Под боем ли фигура

    def is_under_attack(self, row1, col1, color):
        """Метод возвращает True, 
        если поле с координатами (row, col) находится под боем хотя бы одной фигуры цвета color."""
        for i in range(8):
            for j in range(8):
                if self.field[i][j] is not None:
                    piece = self.field[i][j]
                    if piece.get_color() == color:
                        if piece.can_move(row1, col1):
                            return True
        return False

# Рокировка на col = 0

    def castling0(self):
        global flag00, flag01
        
        if self.current_player_color() == WHITE:
            if flag00 is True:
                return False
            rook = self.field[0][0]
            king = self.field[0][4]
            if not isinstance(self.field[0][0], Rook):
                return False
            if not isinstance(self.field[0][4], King):
                return False
            if rook.can_castling0() is False:
                return False
            if king.can_castling0() is False:
                return False
            if self.field[0][2] is not None or self.field[0][3] is not None or \
               self.field[0][1] is not None:
                return False
            if self.is_under_attack(0, 4, self.current_player_color()) is True:
                return False
            self.field[0][0] = None
            self.field[0][4] = None
            self.field[0][2] = King(WHITE)
            self.field[0][3] = Rook(WHITE)
            flag00 = True
            self.color = opponent(self.color)
            return True

        elif self.current_player_color() == BLACK: 
            if flag01 is True:
                return False
            rook = self.field[7][0]
            king = self.field[7][4]
            if not isinstance(self.field[7][0], Rook):
                return False
            if not isinstance(self.field[7][4], King):
                return False
            if rook.can_castling0() is False:
                return False
            if king.can_castling0() is False:
                return False
            if self.is_under_attack(7, 4, self.current_player_color()) is True:
                return False
            if self.field[7][2] is not None or self.field[7][3] is not None or\
               self.field[7][1] is not None:
                return False
            self.field[7][0] = None
            self.field[7][4] = None
            self.field[7][2] = King(BLACK)
            self.field[7][3] = Rook(BLACK)
            self.color = opponent(self.color)
            flag01 = True
            return True

# Рокировка на col = 7

    def castling7(self):
        global flag70, flag71
        
        if self.current_player_color() == WHITE:
            if flag70 is True:
                return False
            rook = self.field[0][7]
            king = self.field[0][4]
            if not isinstance(self.field[0][7], Rook):
                return False
            if not isinstance(self.field[0][4], King):
                return False
            if rook.can_castling0() is False:
                return False
            if king.can_castling0() is False:
                return False
            if self.is_under_attack(0, 4, self.current_player_color()) is True:
                return False
            if self.field[0][5] is not None or self.field[0][6] is not None:
                return False
            self.field[0][4] = None
            self.field[0][7] = None
            self.field[0][6] = King(WHITE)
            self.field[0][5] = Rook(WHITE)
            self.color = opponent(self.color)
            flag70 = True
            return True

        elif self.current_player_color() == BLACK: 
            if flag71 is True:
                return False
            rook = self.field[7][7]
            king = self.field[7][4]
            if not isinstance(self.field[7][7], Rook):
                return False
            if not isinstance(self.field[7][4], King):
                return False
            if rook.can_castling7() is False:
                return False
            if king.can_castling7() is False:
                return False
            if self.is_under_attack(7, 4, self.current_player_color()) is True:
                return False
            if self.field[7][6] is not None or self.field[7][5] is not None:
                return False
            self.field[7][7] = None
            self.field[7][4] = None
            self.field[7][6] = King(BLACK)
            self.field[7][5] = Rook(BLACK)
            self.color = opponent(self.color)
            flag71 = True
            return True

# Ладья


class Rook:

    def __init__(self, color):
        self.color = color
        self.castling0 = True
        self.castling7 = True

    def can_castling0(self):
        if self.castling0 is True:
            return True 
        else:
            return False

    def can_castling7(self):
        if self.castling7 is True:
            return True 
        else:
            return False

    def get_color(self):
        return self.color

    def char(self):
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if row != row1 and col != col1:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            # Если на пути по горизонтали есть фигура
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            # Если на пути по вертикали есть фигура
            if not (board.get_piece(row, c) is None):
                return False

# Проверка на рокировку (Походил- нельзя)
        if col != 0:
            self.castling0 = False
        elif col != 7:
            self.castling7 = False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

# Пешка


class Pawn:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if col != col1:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if row + direction == row1:
            return True

        # ход на 2 клетки из начального положения
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))

# Конь


class Knight:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'N'  # kNight, буква 'K' уже занята королём

    def can_move(self, board, row, col, row1, col1):
        if row + 1 == row1 and col + 2 == col1 or \
           row + 1 == row1 and col - 2 == col1 or \
           row + 2 == row1 and col + 1 == col1 or \
           row + 2 == row1 and col - 1 == col1 or \
           row - 1 == row1 and col + 2 == col1 or \
           row - 1 == row1 and col - 2 == col1 or \
           row - 2 == row1 and col + 1 == col1 or \
           row - 2 == row1 and col - 1 == col1:
            return True
        else: 
            return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)

# Король


class King:

    def __init__(self, color):
        self.color = color
        self.castling0 = True
        self.castling7 = True

    def can_castling0(self):
        if self.castling0 is True:
            return True 
        else:
            return False

    def can_castling7(self):
        if self.castling7 is True:
            return True 
        else:
            return False

    def get_color(self):
        return self.color

    def char(self):
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        if (row + 1 == row1 and col == col1) or \
           (row - 1 == row1 and col == col1) or \
           (row + 1 == row1 and col + 1 == col1) or \
           (row + 1 == row1 and col - 1 == col1) or \
           (row - 1 == row1 and col + 1 == col1) or \
           (row - 1 == row1 and col - 1 == col1) or \
           (col - 1 == col1 and row == row1) or \
           (col + 1 == col1 and row == row1):

            # Проверка на рокировку (Походил- нельзя)
            if col != 0:
                self.castling0 = False
            elif col != 7:
                self.castling7 = False
            return True
        else: 
            return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)

# Ферзь


class Queen:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'Q'

    def can_move(self, board, row, col, row1, col1):
        # Та же клетка
        if row == row1 and col == col1:
            return False
        # Тот же цвета
        if board.get_piece(row1, col1) is not None:
            if self.get_color() == board.get_piece(row1, col1).get_color():
                return False

        # Rook
        if not (row != row1 and col != col1):
            step = 1 if (row1 >= row) else -1
            for r in range(row + step, row1, step):
                if not (board.get_piece(r, col) is None):
                    return False

            step = 1 if (col1 >= col) else -1
            for c in range(col + step, col1, step):
                if not (board.get_piece(row, c) is None):
                    return False
            return True

        # Bishop
        if abs(row - row1) == abs(col - col1):
            step1 = 1 if (row1 >= row) else -1
            step2 = 1 if (col1 >= col) else -1
            c = col + step2
            for r in range(row + step1, row1, step1):
                if not (board.get_piece(r, c) is None):
                    return False
                c = c + step2
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)

# Слон


class Bishop:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        if abs(row - row1) == abs(col - col1):
            step1 = 1 if (row1 >= row) else -1
            step2 = 1 if (col1 >= col) else -1
            c = col + step2
            for r in range(row + step1, row1, step1):
                if not (board.get_piece(r, col) is None):
                    return False
                c = c + step2
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


if __name__ == "__main__":
    main()

# *Дописать шах/мат, отсутствие возможнсти делать рокировку под шахом, окончание игры

