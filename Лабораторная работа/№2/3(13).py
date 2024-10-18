import math

def compute_rectangle_area(a, b):
    return a * b

def compute_ring_area(a, b):
    if a < b:
        return math.pi * (b**2 - a**2)
    else:
        return 0  # Чтобы избежать ошибки, если A >= B

def compute_isosceles_triangle_area(a, b):
    # Для равнобедренного треугольника C равен C = √(A² + B² - 2*A*B*cos(θ)), предположим, что θ = 60°
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(60)))
    # Полусумма для вычисления площади по формуле Герона
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def main():
    print("Введите пары значений A и B, для прекращения ввода внесите пустую строку.")
    while True:
        try:
            user_input = input("Введите A и B (через пробел): ")
            if user_input == '':
                break
            a, b = map(float, user_input.split())
            
            print("Выберите требуемое вычисление:")
            print("1. Площадь прямоугольника с длинами A и B")
            print("2. Площадь кольца с радиусами A и B")
            print("3. Площадь равнобедренного треугольника со сторонами A и B")

            choice = int(input("Ваш выбор (1/2/3): "))

            if choice == 1:
                area = compute_rectangle_area(a, b)
                print(f"Площадь прямоугольника: {area}")

            elif choice == 2:
                area = compute_ring_area(a, b)
                print(f"Площадь кольца: {area}")

            elif choice == 3:
                area = compute_isosceles_triangle_area(a, b)
                print(f"Площадь равнобедренного треугольника: {area}")

            else:
                print("Неверный выбор, попробуйте снова.")

        except ValueError:
            print("Ошибка ввода. Убедитесь, что Вы ввели числовые значения.")

if __name__ == "__main__":
    main()

# Объяснение кода:
#Функции для вычислений: Созданы три функции для вычисления площади прямоугольника, кольца и равнобедренного треугольника.
#Главная функция main: Обеспечивает ввод координат и выбор нужного вычисления. Если пользователь вводит пустую строку, программа завершает ввод.
#Структура многократного выбора: Используется множественный выбор для выбора между вычислениями.
#Обработка ошибок: Программа обрабатывает возможные ошибки при вводе.
