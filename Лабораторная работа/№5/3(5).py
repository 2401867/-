import numpy as np

def count_sign_changes(func, start, end, step):
    """
    Метод для определения количества интервалов смены знака функции.
    
    :param func: Делегат, функция для вычисления значений.
    :param start: Начало интервала.
    :param end: Конец интервала.
    :param step: Шаг.
    :return: Количество интервалов смены знака.
    """
    x_values = np.arange(start, end + step, step)
    y_values = [func(x) for x in x_values]
    
    sign_changes = 0
    for i in range(1, len(y_values)):
        if y_values[i-1] * y_values[i] < 0:
            sign_changes += 1
            
    return sign_changes

# Определяем функции
def func1(x):
    return x**2 - np.sin(x)

def func2(x):
    return np.exp(x) - 1

# Определяем параметры и вызываем метод
sign_changes_func1 = count_sign_changes(func1, 0, 2, 0.1)
sign_changes_func2 = count_sign_changes(func2, -1, 1, 0.2)

print(f"Количество интервалов смены знака для функции y = x^2 - sin(x): {sign_changes_func1}")
print(f"Количество интервалов смены знака для функции y = e^x - 1: {sign_changes_func2}")


#Объяснение:
#count_sign_changes: Метод, который принимает делегат (функцию), начальное и конечное значения интервала, а также шаг. Он вычисляет значения функции на заданном интервале и подсчитывает количество интервалов, где происходит смена знака.
#func1 и func2: Определяют функции, которые мы будем использовать для вычислений.
#Вызов метода: Мы вызываем метод для обеих функций и выводим количество интервалов смены знака.
