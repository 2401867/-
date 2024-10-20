''' 5. Дана матрица A размером 7x5. Максимальный элемент столбца заменть полусуммой первого и 
последнего элементов столбца, если максимальный элемент меньше этой полусуммы, в противном случае 
максимальный элемент заменить его номером в столбце. '''

# Определяем размер матрицы
rows = 7
cols = 5

# Инициализируем матрицу A случайными значениями
import random

A = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

# Функция для замены максимального элемента в каждом столбце
def replace_max_in_columns(matrix):
    for col in range(cols):
        max_value = matrix[0][col]
        max_index = 0
        
        # Находим максимальный элемент и его индекс в столбце
        for row in range(1, rows):
            if matrix[row][col] > max_value:
                max_value = matrix[row][col]
                max_index = row
        
        # Полусумма первого и последнего элементов столбца
        half_sum = (matrix[0][col] + matrix[rows - 1][col]) / 2
        
        # Замена максимального элемента в зависимости от условия
        if max_value < half_sum:
            matrix[max_index][col] = half_sum
        else:
            matrix[max_index][col] = max_index

# Печать исходной матрицы
print("Исходная матрица A:")
for row in A:
    print(row)

# Замена максимальных элементов
replace_max_in_columns(A)

# Печать измененной матрицы
print("\nИзмененная матрица A:")
for row in A:
    print(row)



#    Пояснение кода
#  Инициализация матрицы: Мы создаем матрицу A размером 7x5, заполняя ее случайными целыми числами от 1 до 100.
#  Функция replace_max_in_columns:
    #Для каждого столбца мы находим максимальный элемент и его индекс.
    #Вычисляем полусумму первого и последнего элементов столбца.
    #Если максимальный элемент меньше полусуммы, мы заменяем его на полусумму. В противном случае заменяем его на его индекс в столбце.
#  Вывод: Исходная и измененная матрицы выводятся на экран.
