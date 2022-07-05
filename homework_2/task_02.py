from random import choice

import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        # список пустых ячеек для компьютера
        self.empty_cells = []
        for j in range(height):
            for i in range(width):
                self.empty_cells.append((i, j))
        # чей ход
        self.crosses = True

    def render(self, screen, msg=''):
        # отрисовка поля
        if msg:
            font = pygame.font.Font(None, 25)
            text = font.render(f"Игра окончена! {msg}!", True, (100, 255, 100))
            text_x = 320 // 2 - text.get_width() // 2
            text_y = 345 - text.get_height() // 2
            screen.blit(text, (text_x, text_y))

        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    pygame.draw.line(screen, pygame.Color("blue"),
                                     (self.left + x * self.cell_size + 3,
                                      self.top + y * self.cell_size + 3),
                                     (self.left + x * self.cell_size - 3 + self.cell_size,
                                      self.top + y * self.cell_size - 3 + self.cell_size), 2)
                    pygame.draw.line(screen, pygame.Color("blue"),
                                     (self.left + x * self.cell_size + 3,
                                      self.top + y * self.cell_size + self.cell_size - 3),
                                     (self.left + x * self.cell_size - 3 + self.cell_size,
                                      self.top + y * self.cell_size + 3), 2)
                if self.board[y][x] == 2:
                    pygame.draw.ellipse(screen, pygame.Color("red"), (
                        (self.left + x * self.cell_size + 3, self.top + y * self.cell_size + 3),
                        (self.cell_size - 6, self.cell_size - 6)), 2)
                pygame.draw.rect(screen, pygame.Color("white"), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # cell - кортеж (x, y)
    def on_click(self, cell):
        if self.crosses:
            if self.board[cell[1]][cell[0]] == 0:
                self.board[cell[1]][cell[0]] = 1
                self.crosses = not self.crosses

    # получить ячейку по координатам мыши
    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        if (cell_x, cell_y) in self.empty_cells:
            del self.empty_cells[self.empty_cells.index((cell_x, cell_y))]
        return cell_x, cell_y

    # получить клик пользвателя
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    # ход компьютера (рандомный, выбирает пустую ячейку из списка)
    def step_ii(self):
        if not self.crosses:
            cell_x, cell_y = choice(self.empty_cells)
            self.board[cell_y][cell_x] = 2
            k = 0
            # проверка хода: k - количество попыток
            while self.check_win() == 2:
                self.board[cell_y][cell_x] = 0
                cell_x, cell_y = choice(self.empty_cells)
                self.board[cell_y][cell_x] = 2
                if k == 5:
                    break
                k += 1
            del self.empty_cells[self.empty_cells.index((cell_x, cell_y))]
            self.crosses = not self.crosses

    # проверка победителя
    def check_win(self):
        # пробегаем по строкам, столбцам и диагоналям
        for variant in [self.board, zip(*self.board), self.all_diag()]:
            d = [''.join([str(i) for i in j]) for j in variant]
            if any('11111' in i for i in d):
                print('нолик выиграл')
                return 1
            if any('22222' in i for i in d):
                print('крестик выиграл')
                return 2
            if all('0' not in i for i in d):
                print('ничья')
                return 3
        return 0

    # получить все диагонали доски
    def all_diag(self):
        l = len(self.board)
        b = l * 2 - 1
        ALL_DIAG = [[] for _ in range(b * 2)]
        for i in range(l):
            for j in range(l):
                ALL_DIAG[i + j].append(self.board[j][i])
                ALL_DIAG[i + j + b].append(self.board[~j][i])
        return ALL_DIAG


# перерисовка доски после хода игрока или компьютера
def result_game(screen, board):
    msg = ''
    res = board.check_win()
    print(res)
    if res == 1:
        msg = 'Победа Нолика'
    elif res == 2:
        msg = 'Победа Крестика'
    elif res == 3:
        msg = 'Ничья'
    screen.fill((0, 0, 0))
    board.render(screen, msg)
    pygame.display.flip()


def main():
    pygame.init()
    size = 320, 370
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Обратные крестики-нолики')
    board = Board(10, 10)
    running = True
    screen.fill((0, 0, 0))
    board.render(screen, '')
    pygame.display.flip()
    while running:
        msg = ''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # ход игрока
                board.get_click(event.pos)
                result_game(screen, board)
                # ход компьютера
                board.step_ii()
                result_game(screen, board)

    pygame.quit()


if __name__ == '__main__':
    main()