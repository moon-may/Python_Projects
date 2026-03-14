import random

class Game:

    def __init__(self, cols, rows, mines):
        self.cols = cols
        self.rows = rows
        self.mines = mines
        self.game_over = False

        self.hidden_field = self.create_hidden_field()
        self.player_field = [['#'] * self.cols for _ in range(self.rows)]
        self.flags = [[False for _ in range(cols)] for _ in range(rows)]

    # Скрытое от игрока поле
    def create_hidden_field(self):
        # поле, заполненное нулями
        field = [[0] * self.cols for _ in range(self.rows)]

        # Разместить мины
        mines_placed = 0 # размещенные мины

        while mines_placed < self.mines:
            r = random.randint(0, self.rows - 1) # случайный ряд
            c = random.randint(0, self.cols - 1) # случайный столбец

            # проверка, что мины там нет и добавление
            if field[r][c] != -1:
                field[r][c] = -1
                mines_placed += 1

                # Разместить числа
                # определение соседей
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        # пропустить центр
                        if i == 0 and j == 0:
                            continue
                        # соседи
                        nr = r + i
                        nc = c + j
                        # проверка границ
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            # если клетка - не мина
                            if field[nr][nc] != -1:
                                field[nr][nc] += 1

        return field
    
    # Открыть клетку
    def open_cell(self, row, col):
        '''
        проверь границы
        проверь, стоит ли флаг, если стоит - не открывай, попроси другие координаты или сменить флаг
        проверь, открыта ли клетка. если открыта - выведи запрос на другие координаты
        если закрыта и мина - закончить игру, показать поле
        если закрыта и цифра - выведи цифру
        если закрыта и 0 - самовызов на соседние клетки
        '''
        if not(0 <= row < self.rows and 0 <= col < self.cols):
            return 'INVALID_COORDS'     # координаты не существуют
        elif self.flags[row][col]:
            return 'HAS_FLAG'           # уже стоит флаг
        elif self.player_field[row][col] != '#':
            return 'ALREADY_OPEN'       # уже открыта клетка
        elif self.hidden_field[row][col] == -1:
            self.game_over = True       
            return 'MINE'               # в клетке мина
        
        cell_value = self.hidden_field[row][col]
        self.player_field[row][col] = str(self.hidden_field[row][col])

        if cell_value == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    nr = row + i
                    nc = col + j
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        if self.player_field[nr][nc] == '#' and not self.flags[nr][nc]:
                            self.open_cell(nr, nc)


    # Смена флага
    def toggle_flag(self):
        pass


    # Состояние игры
    def game_status(self):
        pass
