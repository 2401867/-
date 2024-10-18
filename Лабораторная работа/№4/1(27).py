import random

def generate_matrix(rows, cols):
    """Генерирует матрицу размером rows x cols с случайными значениями."""
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix):
    """Выводит матрицу на экран."""
    for row in matrix:
        print(' '.join(map(str, row)))

def replace_column_with_max(matrix):
    """
    Заменяет 4-й столбец матрицы массивом, состоящим из максимальных элементов строк, расположенных в обратном порядке.
    """
    # Получаем максимальные элементы строк
    max_elements = [max(row) for row in matrix]
    
    # Заменяем 4-й столбец на элементы max_elements в обратном порядке
    for i in range(len(matrix)):
        matrix[i][3] = max_elements[len(max_elements) - 1 - i]
    
    return matrix

# Размерность матрицы
rows, cols = 5, 7

# Генерация и вывод исходной матрицы
matrix = generate_matrix(rows, cols)
print("Исходная матрица:")
print_matrix(matrix)

# Замена 4-го столбца и вывод результата
matrix = replace_column_with_max(matrix)
print("\nМатрица после замены 4-го столбца:")
print_matrix(matrix)


#   Пояснения к коду:
# Функция generate_matrix: генерирует матрицу с заданными размерами, заполняя ее случайными числами от 1 до 100.
# Функция print_matrix: выводит матрицу на экран в удобочитаемом формате.
# Функция replace_column_with_max:
   #Сначала она извлекает максимальные элементы из каждой строки, создавая одномерный массив max_elements.
   #Затем эта функция заменяет 4-й столбец на элементы массива max_elements, расположенные в обратном порядке.
# Основная часть программы:
   #Определяет размеры матрицы (5 строк, 7 столбцов).
   #Генерирует и выводит исходную матрицу.
   #Заменяет 4-й столбец и выводит измененную матрицу.
