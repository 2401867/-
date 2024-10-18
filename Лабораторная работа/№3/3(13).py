def remove_duplicates(arr):
    # Используем множество (set) для удаления дубликатов
    unique_elements = set(arr)
    # Преобразуем множество обратно в список
    return list(unique_elements)

# Ввод данных
input_array = [int(x) for x in input("Введите элементы массива через пробел: ").split()]

# Печатаем исходный массив
print(f"Исходный массив: {input_array}")

# Удаляем повторяющиеся элементы
result_array = remove_duplicates(input_array)

# Печатаем результат
print(f"Массив без повторяющихся элементов: {result_array}")



#    Объяснение кода:
# Функция remove_duplicates:
#Принимает массив arr в качестве входного параметра.
#Преобразует массив в множество (set), чтобы автоматически избавиться от дубликатов, так как множества не могут содержать одинаковых элементов.
#Возвращает новое множество, преобразованное обратно в список.

# Ввод данных:
#Запрашивает у пользователя ввод элементов массива через пробел.
#Преобразует введённые строки в список целых чисел с помощью списка-генератора.

# Печать исходного массива:
#Отображает исходный массив до удаления дубликатов.

# Удаление дубликатов:
#Вызывает функцию remove_duplicates для обработки введенного массива.
#Печать результата:
#Отображает массив без повторяющихся элементов.
