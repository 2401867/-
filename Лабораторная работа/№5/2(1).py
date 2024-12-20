import numpy as np

def find_max_element(matrix):
    """
    Находит максимальный элемент в матрице.
    
    Параметры:
    matrix (np.ndarray): Входная матрица.
    
    Возвращаемое значение:
    tuple: Координаты максимального элемента (строка, столбец) и его значение.
    """
    max_value = np.max(matrix)
    max_index = np.unravel_index(np.argmax(matrix), matrix.shape)
    return max_index, max_value

def swap_max_elements(matrix_a, matrix_b):
    """
    Меняет местами максимальные элементы двух матриц.
    
    Параметры:
    matrix_a (np.ndarray): Первая матрица.
    matrix_b (np.ndarray): Вторая матрица.
    
    Возвращаемое значение:
    tuple: Обновленные матрицы.
    """
    # Находим максимальные элементы
    (row_a, col_a), max_a = find_max_element(matrix_a)
    (row_b, col_b), max_b = find_max_element(matrix_b)
    
    # Меняем местами максимальные элементы
    matrix_a[row_a, col_a] = max_b
    matrix_b[row_b, col_b] = max_a
    
    return matrix_a, matrix_b

# Пример использования
matrix_a = np.random.randint(1, 100, (5, 6))
matrix_b = np.random.randint(1, 100, (3, 5))

print("Матрица A:")
print(matrix_a)
print("Матрица B:")
print(matrix_b)

# Меняем местами максимальные элементы
updated_matrix_a, updated_matrix_b = swap_max_elements(matrix_a, matrix_b)

print("Обновленная матрица A:")
print(updated_matrix_a)
print("Обновленная матрица B:")
print(updated_matrix_b)


#Объяснение:
#find_max_element: Метод для поиска максимального элемента в матрице. Он принимает матрицу как входной параметр и возвращает координаты максимального элемента и его значение.
#swap_max_elements: Метод, который принимает две матрицы, находит их максимальные элементы и меняет их местами. Он возвращает обновленные матрицы.
#Пример использования: Создаются две матрицы с случайными значениями, и затем вызывается метод для обмена их максимальными элементами.
