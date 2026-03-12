import random

# Скрытое от игрока поле
def create_hidden_field(cols, rows, mines):
    field = []

    # Задать поле
    for row in range(rows): # для каждой строки
        row = []
        for col in range(cols): # для каждого столбца
            row.append(0) # добавить 0 в строку
        field.append(row) # добавить строки в поле

    # Разместить мины
    mines_placed = 0 # размещенные мины

    while mines_placed < mines:
        r = random.randint(0, rows - 1) # случайный ряд
        c = random.randint(0, cols - 1) # случайный столбец

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
                    if 0 <= nr < rows and 0 <= nc < cols:
                        # если клетка - не мина
                        if field[nr][nc] != -1:
                            field[nr][nc] += 1

    return field


# Поле игрока
def create_user_field(cols, rows):
    user_field = []

    for row in range(rows):
        row = []
        for col in range(cols):
            row.append('#')
        user_field.append(row)



