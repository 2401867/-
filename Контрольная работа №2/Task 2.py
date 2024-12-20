''' 24. В двух заданных квадратных матрицах столбец, содержащий максимальный элемент матрицы, поменять местами с главной диагональю. Поиск максимального элемента и дальнейшее преобразование матрицы оформить в виде методов.'''


class Matrix:
    def __init__(self, data):
        self.data = data
        self.size = len(data)

    def find_max_column(self):
        max_value = float('-inf')
        max_column_index = -1
        for j in range(self.size):
            for i in range(self.size):
                if self.data[i][j] > max_value:
                    max_value = self.data[i][j]
                    max_column_index = j
        return max_column_index

    def swap_with_diagonal(self, column_index):
        for i in range(self.size):
            self.data[i][column_index], self.data[i][i] = self.data[i][i], self.data[i][column_index]

    def print_matrix(self):
        for row in self:
            print(" ".join(map(str, row)))
            print()  # Для разделения выводов

# Пример использования
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix = Matrix(matrix_data)

print("Исходная матрица:")
matrix.print_matrix()

max_column = matrix.find_max_column()
print(f"Столбец с максимальным элементом: {max_column}")

matrix.swap_with_diagonal(max_column)

print("Матрица после замены столбца с максимальным элементом и главной диагональю:")
matrix.print_matrix()



#Объяснение:
#Класс Matrix: Определяет матрицу и методы для работы с ней.
#Метод find_max_column: Находит индекс столбца с максимальным элементом.
#Метод swap_with_diagonal: Меняет местами элементы указанного столбца с элементами главной диагонали.
#Метод print_matrix: Печатает матрицу.
