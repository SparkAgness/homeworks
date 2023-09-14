# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

import random

class Matrixx:
    def __init__(self, strings, rows, n, memb=None):
        self.rows = rows
        self.strings = strings
        self.n = n
        self.memb = []
        self.help_memb = []
        for i in range(self.strings):
            for j in range(self.rows):
                random.seed()
                memb_ij = random.randint(0, self.n)
                if 10 < memb_ij < 198:
                    self.help_memb.append(None)
                else:
                    self.help_memb.append(memb_ij)
            self.memb.append(self.help_memb)
            self.help_memb = []
                
    def __repr__(self):        
        self.main_string = ""
        for i in range(self.strings):
            self.help_string = ""            
            self.help_string = '[' + ', '.join(str(el) for el in self.memb[i]) + ']' + '\n'
            self.main_string += self.help_string
        return self.main_string

    def new_value(self, strings, rows, value):        
        if (strings >= len(self.memb) or rows >= len(self.memb[0])):
            print("Incorrect value of string or row of matrix")
            return
        self.memb[strings][rows] = value
        return self.memb
            
    def change_value(self, new_value, old_value):
        for i in range(len(self.memb)):
            for j in range (len(self.memb[i])):
                if self.memb[i][j] == old_value:
                    self.memb[i][j] = new_value
        return self.memb
        
    def sizes(self):
        print(f"Strings are: {len(self.memb)}, rows are: {len(self.memb[0])}")

chess_board = Matrixx(8, 8, 589)
print(chess_board)
chess_board.new_value(7, 7, 1)
chess_board.new_value(0, 0, 1)
print(chess_board)
chess_board.change_value(13, None)
print(chess_board)
chess_board.sizes()
