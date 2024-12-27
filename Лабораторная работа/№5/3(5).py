''' 5. Разработать метод определения количества интервалов смены знака функции, заданной таблично на отрезке с постоянным шагом аргумента. Решить задачу для функции у = х²- sin x на отрезке [0, 2] с шагом 0,1 и функции у = е^x - 1 на отрезке [-1, 1] с шагом 0,2. Для вычисления очередного значения функции использовать делегат.'''

import math

# Делегат для вычисления значения функции
def function_delegate(func, x):
    return func(x)

# Функции для вычисления
def func1(x):
    return x**2 - math.sin(x)

def func2(x):
    return math.exp(x) - 1

# Метод для определения количества интервалов смены знака
def count_sign_changes(func, start, end, step):
    count = 0
    previous_value = function_delegate(func, start)
    
    x = start + step
    while x <= end:
        current_value = function_delegate(func, x)
        if previous_value * current_value < 0:  # Смена знака
            count += 1
        previous_value = current_value
        x += step
    
    return count

# Проверка кода с переменными True и False
if __name__ == "__main__":
    # Для функции y = x^2 - sin(x) на отрезке [0, 2] с шагом 0.1
    sign_changes_func1 = count_sign_changes(func1, 0, 2, 0.1)
    print(f"Количество интервалов смены знака для функции 1: {sign_changes_func1}")

    # Для функции y = e^x - 1 на отрезке [-1, 1] с шагом 0.2
    sign_changes_func2 = count_sign_changes(func2, -1, 1, 0.2)
    print(f"Количество интервалов смены знака для функции 2: {sign_changes_func2}")
