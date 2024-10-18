''' 7. В компьютер вводится координаты n точек, лежащих на плоскасти. После ввода координат 
каждой точке выводить номер квадранта, в котором она находится. Определить количество  точек, 
лежащих по отдельности в 1-м и 3-м квадрантах. '''

def get_quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return 0  # Точка лежит на оси

def main():
    n = int(input("Введите количество точек: "))
    count_first_quadrant = 0
    count_third_quadrant = 0

    for i in range(n):
        x = float(input(f"Введите координату x для точки {i + 1}: "))
        y = float(input(f"Введите координату y для точки {i + 1}: "))
        
        quadrant = get_quadrant(x, y)
        
        if quadrant == 1:
            print(f"Точка {i + 1} находится в 1-м квадранте.")
            count_first_quadrant += 1
        elif quadrant == 2:
            print(f"Точка {i + 1} находится во 2-м квадранте.")
        elif quadrant == 3:
            print(f"Точка {i + 1} находится в 3-м квадранте.")
            count_third_quadrant += 1
        elif quadrant == 4:
            print(f"Точка {i + 1} находится в 4-м квадранте.")
        else:
            print(f"Точка {i + 1} лежит на оси.")

    print(f"Количество точек в 1-м квадранте: {count_first_quadrant}")
    print(f"Количество точек в 3-м квадранте: {count_third_quadrant}")

if __name__ == "__main__":
    main()


# Список используемых переменных:
#n - количество точек.
#count_first_quadrant - счетчик точек в 1-м квадранте.
#count_third_quadrant - счетчик точек в 3-м квадранте.
#x - координата x точки.
#y - координата y точки.
#quadrant - номер квадранта, в котором находится точка.
    
