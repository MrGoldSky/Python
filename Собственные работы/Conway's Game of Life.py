import numpy as np
import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color("white"), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    def get_cell(self, mouse_pos):
        if self.left < mouse_pos[0] < self.left + self.width * self.cell_size:
            if self.top < mouse_pos[1] < self.top + self.height * self.cell_size:
                x = (mouse_pos[1] - self.left) // self.cell_size
                y = (mouse_pos[0] - self.top) // self.cell_size
                return (x, y)
        return None

    def on_click(self, cell_coords):
        self.board[cell_coords[0]][cell_coords[1]] = 1
        pygame.draw.rect(screen, pygame.Color(f"Blue"), (cell_coords[1] * self.cell_size + self.left, cell_coords[0] * self.cell_size + self.top, 
                                                        self.cell_size, self.cell_size), 0)
        board.render(screen)
        pygame.display.flip()
        
    
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell != None:
            self.on_click(cell)
        else:
            print(None)
    
    def go_board(self, board):
        global screen
        self.board = board.tolist()
        board = board.tolist()
        screen = pygame.display.set_mode(size)
        self.render(screen)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    self.on_click([i, j])


class life(Board):
    
    def __init__(self, width, height):
        super().__init__(width, height)

    def next_move(self):
        self.board_life = np.array(self.board, dtype=np.uint8)
        neighbors = sum([
            np.roll(np.roll(self.board_life, -1, 1), 1, 0),
            np.roll(np.roll(self.board_life, 1, 1), -1, 0),
            np.roll(np.roll(self.board_life, 1, 1), 1, 0),
            np.roll(np.roll(self.board_life, -1, 1), -1, 0),
            np.roll(self.board_life, 1, 1),
            np.roll(self.board_life, -1, 1),
            np.roll(self.board_life, 1, 0),
            np.roll(self.board_life, -1, 0)
        ])
        print(self.board_life)
        self.board_life = ((neighbors == 3) | (self.board_life & (neighbors == 2))).copy()
        super().go_board(self.board_life)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Игра «Жизнь»')
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    running = True
    screen = pygame.display.set_mode(size)
    board = life(10, 10)
    fps = 60
    clock = pygame.time.Clock()
    
    k = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False        
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
                if event.button == 5:
                    fps += 2
                    print(fps)
                if event.button == 4:
                    fps -= 2
                    print(fps)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    k += 1
            if k % 2 == 0:
                clock.tick(fps)
                board.next_move()
        board.render(screen)
        pygame.display.flip()