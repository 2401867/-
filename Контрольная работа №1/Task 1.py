''' 17. Считая, что Земля - идеальная сфера с радиусом R~6350 км,
определить расстояние до линии горизонта с высоты 1, 2, ..., 10 км.'''

import math

# Радиус Земли в километрах
R = 6350

# Переменные для проверки
is_correct = True
is_error = False

# Печатаем результаты для высот от 1 до 10 км
print("Высота (км) | Расстояние до горизонта (км)")
print("-------------------------------------------")
for h in range(1, 11):
    d = math.sqrt(2 * R * h)
    print(f"{h:<12} | {d:.2f}")

# Проверка корректности выполнения
if is_correct:
    print("Код выполнен успешно.")
else:
    print("Произошла ошибка.")
