 #Вариант 1: Двухмерный массив
def create_matrix(n):
    """Создает матрицу n x n с случайными числами."""
    import random
    return [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

def extract_triangles(matrix):
    """Извлекает верхний и нижний треугольники из матрицы."""
    n = len(matrix)
    upper_triangle = []
    lower_triangle = []

    for i in range(n):
        for j in range(n):
            if j >= i:  # Верхний треугольник
                upper_triangle.append(matrix[i][j])
            if j <= i:  # Нижний треугольник
                lower_triangle.append(matrix[i][j])

    return upper_triangle, lower_triangle

def print_triangles(upper, lower):
    """Печатает верхний и нижний треугольники."""
    print("Верхний треугольник:")
    print(upper)
    print("Нижний треугольник:")
    print(lower)

# Пример использования
n = 5  # Размер матрицы
matrix = create_matrix(n)
upper_triangle, lower_triangle = extract_triangles(matrix)
print_triangles(upper_triangle, lower_triangle)


#Вариант 2: Одномерная последовательность
def create_flat_matrix(n):
    """Создает одномерный массив, представляющий матрицу n x n."""
    import random
    return [random.randint(1, 100) for _ in range(n * n)]

def extract_triangles_flat(flat_matrix, n):
    """Извлекает верхний и нижний треугольники из одномерного массива."""
    upper_triangle = []
    lower_triangle = []

    for i in range(n):
        for j in range(n):
            index = i * n + j
            if j >= i:  # Верхний треугольник
                upper_triangle.append(flat_matrix[index])
            if j <= i:  # Нижний треугольник
                lower_triangle.append(flat_matrix[index])

    return upper_triangle, lower_triangle

def print_triangles_flat(upper, lower):
    """Печатает верхний и нижний треугольники из одномерного массива."""
    print("Верхний треугольник:")
    print(upper)
    print("Нижний треугольник:")
    print(lower)

# Пример использования
n = 5  # Размер матрицы
flat_matrix = create_flat_matrix(n)
upper_triangle, lower_triangle = extract_triangles_flat(flat_matrix, n)
print_triangles_flat(upper_triangle, lower_triangle)




#   Пояснение кода :
# Создание матрицы: В обоих вариантах мы создаем матрицу (двумерную или одномерную) с случайными числами.
# Извлечение треугольников: Мы проходим по элементам матрицы и добавляем их в соответствующие массивы в зависимости от их положения (верхний или нижний треугольник).
# Печать результатов: В конце мы выводим полученные массивы.



