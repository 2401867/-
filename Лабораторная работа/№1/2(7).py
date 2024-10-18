# Задание a: подсчёт общего пути за 7 дней
initial_distance = 10  # Начальное расстояние в км
daily_increase = 0.10  # Увеличение на 10%
total_distance_7_days = 0

for day in range(7):
    # Каждый день увеличиваем путь на 10%
    if day > 0:
        initial_distance *= (1 + daily_increase)
    
    total_distance_7_days += initial_distance

print(f"Суммарный путь спортсмена за 7 дней: {total_distance_7_days:.2f} км")

# Задание б: найти количество дней для преодоления 100 км
initial_distance = 10
total_distance = 0
days_for_100_km = 0

while total_distance < 100:
    total_distance += initial_distance
    initial_distance *= (1 + daily_increase)
    days_for_100_km += 1

print(f"Количество дней, чтобы пробежать 100 км: {days_for_100_km}")

# Задание в: количество дней для пробежки более 20 км
initial_distance = 10
days_for_20_km = 0

while initial_distance <= 20:
    initial_distance *= (1 + daily_increase)
    days_for_20_km += 1

print(f"Количество дней для пробежки более 20 км: {days_for_20_km}")


# Объяснение:
# Задание a: Используется цикл for для подсчета общего пробега спортсмена за 7 дней. Каждый день увеличивается дистанция на 10%, и она добавляется к общей дистанции.

# Задание б: Используется цикл while, который продолжает выполняться, пока суммарный пробег меньше 100 км. Каждый день добавляется дистанция, и счётчик дней увеличивается.

# Задание в: Используется цикл while, который продолжается, пока дневная дистанция не превысит 20 км. Счётчик дней также увеличивается на каждом шаге.

