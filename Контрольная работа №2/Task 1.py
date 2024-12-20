# 29. В матрице F размером 5 х 7 удалить столбец, расположенный после столбца, содержащего минимальный по модулю элемент во 2-й строке.

import numpy as np

class MatrixProcessor:
    def __init__(self, matrix):
        self.matrix = matrix

    def print_matrix(self, title):
        print(f"{title}:")
        print(self.matrix)

    def remove_column_after_min(self):
        # Находим индекс минимального по модулю элемента во 2-й строке
        min_index = np.argmin(np.abs(self.matrix[1]))
        
        # Удаляем столбец, расположенный после найденного индекса
        if min_index + 1 < self.matrix.shape[1]:  # Проверяем, что есть столбец для удаления
            self.matrix = np.delete(self.matrix, min_index + 1, axis=1)

# Пример использования
if __name__ == "__main__":
    # Исходная матрица 5x7
    F = np.array([[1, 2, 3, 4, 5, 6, 7],
                  [8, -9, 10, 11, 12, 13, 14],
                  [15, 16, 17, 18, 19, 20, 21],
                  [22, 23, 24, 25, 26, 27, 28],
                  [29, 30, 31, 32, 33, 34, 35]])

    processor = MatrixProcessor(F)
    processor.print_matrix("Исходная матрица")
    processor.remove_column_after_min()
    processor.print_matrix("Матрица после удаления столбца")


#Объяснение:
#Класс MatrixProcessor: Этот класс принимает матрицу и содержит методы для печати матрицы и удаления столбца.
#Метод remove_column_after_min: Находит индекс минимального по модулю элемента во второй строке и удаляет столбец, который следует за ним.
#Пример использования: Создается матрица F, и с помощью методов класса выводятся исходные данные и результат.
