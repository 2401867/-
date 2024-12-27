''' 6. В компьютер по очереди вводятся координаты n точек. Определить, сколько из них принадлежит фигуре, ограниченной осью абсцисс и аркой синусоиды, построенной для аргумента от 0 до п.'''

import math

def is_point_inside_sine_arc(x, y):
    """Проверяет, находится ли точка (x, y) под аркой синусоиды."""
    return y >= 0 and y <= math.sin(x) and 0 <= x <= math.pi

def main():
    count_inside = 0
    print("Введите координаты точек (x, y). Для завершения ввода нажмите Ctrl+D (Linux/Mac) или Ctrl+Z (Windows):")
    
    try:
        while True:
            line = input()
            x, y = map(float, line.split())
            if is_point_inside_sine_arc(x, y):
                count_inside += 1
    except EOFError:
        pass  # Конец ввода

    print(f"Количество точек, принадлежащих фигуре: {count_inside}")

if __name__ == "__main__":
    main()
