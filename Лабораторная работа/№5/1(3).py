''' 3. Два велосипедиста одновременно начинают движение из одной точки. Первый начинает движение со скоростью 10 км/ч и равномерно увеличивает скорость на 1 км/ч. Второй начинает движение со скоростью 9 км/ч и равномерно увеличивает скорость на 1,6 км/ч. Опре- делить:
а) какой спортсмен преодолеет большее расстояние через 1 ч, через 4 ч;
б) когда второй спортсмен догонит первого.
Использовать метод для вычисления пути в зависимости от време- ни по формуле
S = vt + ar²/2,
где v начальная скорость;
а- ускорение. '''


class Cyclist:
    def __init__(self, initial_speed, acceleration):
        self.initial_speed = initial_speed
        self.acceleration = acceleration

    def calculate_distance(self, time):
        """Вычисляет расстояние на основе времени с использованием формулы S = vt + at^2/2"""
        return self.initial_speed * time + (self.acceleration * time**2) / 2

def main():
    # Создаем объекты для двух спортсменов
    cyclist1 = Cyclist(initial_speed=10, acceleration=1)
    cyclist2 = Cyclist(initial_speed=9, acceleration=1.6)

    # Время в часах
    times = [1, 4]

    # a) Расчет расстояний для обоих спортсменов
    for time in times:
        distance1 = cyclist1.calculate_distance(time)
        distance2 = cyclist2.calculate_distance(time)
        print(f"Через {time} ч: Велосипедист 1 проедет {distance1:.2f} км, Велосипедист 2 проедет {distance2:.2f} км")

    # b) Определение момента, когда второй спортсмен догонит первого
    time = 0
    while True:
        distance1 = cyclist1.calculate_distance(time)
        distance2 = cyclist2.calculate_distance(time)
        if distance2 >= distance1:
            break
        time += 0.01  # Увеличиваем время с шагом 0.01 ч для точности

    print(f"Второй спортсмен догонит первого через {time:.2f} ч.")

if __name__ == "__main__":
    main()



#Объяснение кода:
    #Класс Cyclist:
    #Определяет велосипедиста с начальными параметрами скорости и ускорения.
    #Метод calculate_distance вычисляет расстояние, преодоленное велосипедистом за заданное время, согласно формуле ( S = vt + \frac{1}{2}ar^2 ).
    #Функция main():
    #Создает объекты для двух велосипедистов с заданными начальными скоростями и ускорениями.
    #Вычисляет и выводит расстояния, которые проедут оба велосипедиста через 1 и 4 часа.
    #Использует цикл для нахождения момента времени, когда второй велосипедист догонит первого, увеличивая время постепенно и сравнивая расстояния.
#Входные параметры методов:
    #time: время (в часах) для вычисления расстояния, передаваемое методу calculate_distance.
#Возвращаемое значение:
    #Метод calculate_distance возвращает расстояние, пройденное велосипедистом за установленное время.
