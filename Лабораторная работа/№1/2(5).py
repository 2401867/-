''' 5. Определить частное и остаток от деления двух целых чисел N и М, используя операцию вычитания. '''


def division_using_subtraction(N, M):
    # Проверка на деление на ноль
    if M == 0:
        return "Ошибка: деление на ноль"

    quotient = 0
    remainder = N

    # Цикл для нахождения частного и остатка
    while remainder >= M:
        remainder -= M
        quotient += 1

    return quotient, remainder

# Примеры проверки кода
N_true = 10
M_true = 3
result_true = division_using_subtraction(N_true, M_true)
print(f"Частное: {result_true[0]}, Остаток: {result_true[1]}")

N_false = 10
M_false = 0
result_false = division_using_subtraction(N_false, M_false)
print(result_false)
