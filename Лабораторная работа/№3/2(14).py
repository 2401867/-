''' 14. Поменять местами максимальный и первый отрицательный элементы массива. '''

def swap_max_and_first_negative(arr):
    if not arr:  # Проверка на пустой массив
        return arr
    
    # Находим максимальный элемент
    max_index = arr.index(max(arr))
    
    # Находим первый отрицательный элемент
    first_negative_index = next((i for i, x in enumerate(arr) if x < 0), None)
    
    if first_negative_index is not None:
        # Меняем местами
        arr[max_index], arr[first_negative_index] = arr[first_negative_index], arr[max_index]
    
    return arr

# Пример ввода
original_array = [3, -1, 7, 5, -2, 1, 4, 8]
print("Исходный массив:", original_array)

# Выполняем замену
result_array = swap_max_and_first_negative(original_array.copy())

print("Массив после замены:", result_array)



#  Пояснение программы:
#Функция swap_max_and_first_negative принимает массив на вход.
#Проверяет, что массив не пуст.
#Находит индекс максимального элемента в массиве.
#Находит индекс первого отрицательного элемента.
#Если отрицательный элемент найден, то меняет местами максимальный и первый отрицательный элементы.
#Возвращает изменённый массив.
