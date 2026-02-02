import tkinter as tk
import math

#   Класс для простого режима калькулятора
class App:
    #   Инициализация класса
    def __init__(self):
        self.root = root
        self.root.title('Калькулятор')

        self.current = '0'
        self.operation = None
        self.first_op = None
        self.mem_check = True
        self.memory = 0

        self.create_app()

    #   Создание графического интерфейса простого режима
    def create_app(self):
        self.root.geometry('400x400')
        self.input_entry = tk.Entry(self.root, font=('Arial', '40'), justify='right')
        self.input_entry.pack(fill=tk.X, padx=15, pady=10, ipady=5)
        self.input_entry.insert(0, self.current)

        #   Создание кнопок
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill=tk.BOTH, expand=True)

        buttons = [('C', 0, 4),
                   ('MC', 1, 0), ('MR', 1, 1), ('MS', 1, 2), ('M+', 1, 3), ('M-', 1, 4),
                   ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3), ('x^y', 2, 4),
                   ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), ('√', 3, 4),
                   ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), ('+/-', 4, 4),
                   ('0', 5, 1), ('.', 5, 2), ('+', 5, 3), ('=', 5, 4)]

        for (text, row, column) in buttons:
            btn = tk.Button(btn_frame, text=text, font=20,
                            command=lambda t=text: self.button_click(t))
            if text in ('MC', 'MR', 'MS', 'M+', 'M-'):
                btn.config(bg='#87CEEB')
            elif text == 'C':
                btn.config(bg='#FF4500')
            elif text == '=':
                btn.config(bg='#00BFFF')
            elif text not in ('1234567890.'):
                btn.config(bg='#808080')
            btn.grid(row=row, column=column, sticky='nsew', pady=3, padx=3)

        for i in range(5):
            btn_frame.grid_columnconfigure(index=i, weight=1)
        for i in range(6):
            btn_frame.grid_rowconfigure(index=i, weight=1)

    #   Обновление дисплея
    def update_display(self):
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, self.current)

    #   Привязка функций к соответствующим кнопкам
    def button_click(self, button_text):
        if button_text in ('1234567890'):
            self.input_digit(button_text)
        elif button_text == '.':
            self.input_dot()
        elif button_text in '+-*/':
            self.set_operation(button_text)
        elif button_text == 'x^y':
            self.set_operation('^')
        elif button_text == '√':
            self.sqrt_calc()
        elif button_text == '=':
            self.calculate()
        elif button_text == 'C':
            self.clear()
        elif button_text == '+/-':
            self.change_sign()
        elif button_text in ('MC', 'MR', 'MS', 'M+', 'M-'):
            self.memory_ops(button_text)

    #   Ввод цифр
    def input_digit(self, digit):
        if self.mem_check or self.current == '0':
            self.current = digit
            self.mem_check = False
        else:
            self.current += digit
        self.update_display()

    #   Ввод десятичной точки
    def input_dot(self):
        if '.' not in self.current:
            self.current += '.'
            self.update_display()

    #   Реакция на ввод арифметических операций
    def set_operation(self, op):
        self.first_op = float(self.current)
        self.current = '0'
        self.operation = op

    #   Вычисление квадратного корня только из положительных или нуля
    def sqrt_calc(self):
        value = float(self.current)
        if value >= 0:
            result = math.sqrt(value)
            self.current = str(int(result) if result.is_integer() else result)
        else:
            self.current = 'ERROR'
        self.update_display()

    #   Вычисление арифметических действий
    def calculate(self):
        second_op = float(self.current)
        result = None
        try:
            if self.operation == '+':
                result = self.first_op + second_op
            elif self.operation == '-':
                result = self.first_op - second_op
            elif self.operation == '*':
                result = self.first_op * second_op
            elif self.operation == '/':
                result = self.first_op / second_op
            elif self.operation == '^':
                result = self.first_op ** second_op
            self.current = str(int(result) if result.is_integer() else result)
            self.first_op = result
        #   Запрет деления на ноль
        except ZeroDivisionError:
            self.current = 'ERROR'
            self.first_op = None
        self.mem_check = True
        self.update_display()

    #   Обработка кнопки сброса
    def clear(self):
        self.current = '0'
        self.first_op = None
        self.mem_check = True
        self.operation = None
        self.update_display()

    #   Обработка смены знака
    def change_sign(self):
        if self.current == '0':
            self.current = '-'
            self.mem_check = False
        elif self.current == '-':
            self.current = '0'
        elif self.current[0] == '-':
            self.current = self.current[1:]
        else:
            self.current = '-' + self.current
        self.update_display()

    #   Работа с памятью
    def memory_ops(self, mem_command):
        current_val = float(self.current)
        if mem_command == 'MC':
            self.memory = 0
        elif mem_command == 'MR':
            self.current = str(self.memory)
            self.update_display()
        elif mem_command == 'MS':
            self.memory = current_val
        elif mem_command == 'M+':
            self.memory += current_val
        elif mem_command == 'M-':
            self.memory -= current_val


root = tk.Tk()
app = App()
root.mainloop()
