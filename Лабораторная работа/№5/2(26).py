''' 26. В двух заданных матрицах одинакового размером поменять строки, содержащие максимальное количество отрицательных элементов. Нахождение количества отрицательных элементов заданной строки матрицы осуществлять в методе. Определение номера строки, содержащей максимальное количество отрицательных элементов, осуществлять в методе.'''


import numpy as np

class MatrixManipulator:
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def count_negative_elements(self, row):
        """Метод для подсчета количества отрицательных элементов в строке."""
        return sum(1 for x in row if x < 0)

    def row_with_max_negatives(self, matrix):
        """Метод для нахождения номера строки с максимальным количеством отрицательных элементов."""
        max_negatives = -1
        row_index = -1
        for i, row in enumerate(matrix):
            count = self.count_negative_elements(row)
            if count > max_negatives:
                max_negatives = count
                row_index = i
        return row_index

    def swap_rows(self):
        """Метод для замены строк с максимальным количеством отрицательных элементов в двух матрицах."""
        row1 = self.row_with_max_negatives(self.matrix1)
        row2 = self.row_with_max_negatives(self.matrix2)

        # Меняем строки местами
        self.matrix1[row1], self.matrix2[row2] = self.matrix2[row2], self.matrix1[row1]

    def display_matrices(self):
        """Метод для отображения матриц."""
        print("Matrix 1:")
        print(self.matrix1)
        print("Matrix 2:")
        print(self.matrix2)

# Пример использования
matrix1 = np.array([[1, -2, 3], [-1, -4, 5], [6, 7, -8]])
matrix2 = np.array([[9, -10, 11], [12, 13, -14], [-15, 16, 17]])

manipulator = MatrixManipulator(matrix1, matrix2)
print("Before swapping:")
manipulator.display_matrices()

manipulator.swap_rows()

print("\nAfter swapping:")
manipulator.display_matrices()


#Объяснение:
    #Класс MatrixManipulator: Содержит методы для работы с матрицами.
    #Метод count_negative_elements: Подсчитывает количество отрицательных элементов в заданной строке.
    #Метод row_with_max_negatives: Находит строку с максимальным количеством отрицательных элементов.
    #Метод swap_rows: Меняет строки с максимальным количеством отрицательных элементов между двумя матрицами.
    #Метод display_matrices: Выводит матрицы на экран.
