class Student:
    def __init__(self, surname, group, scores):
        self.surname = surname
        self.group = group
        self.scores = scores

    def average_score(self):
        return sum(self.scores) / len(self.scores)

def main():
    students = []
    num_students = int(input("Введите количество студентов: "))

    for _ in range(num_students):
        surname = input("Введите фамилию студента: ")
        group = input("Введите группу студента: ")
        scores = list(map(float, input("Введите результаты экзаменов через пробел: ").split()))
        students.append(Student(surname, group, scores))

    # Фильтрация студентов с средним баллом не менее 4
    qualified_students = [student for student in students if student.average_score() >= 4]

    # Сортировка студентов по среднему баллу в порядке убывания
    qualified_students.sort(key=lambda student: student.average_score(), reverse=True)

    # Вывод результатов
    print("\nСтуденты с средним баллом не менее 4:")
    print(f"{'Фамилия':<20} {'Группа':<10} {'Средний балл':<15}")
    for student in qualified_students:
        print(f"{student.surname:<20} {student.group:<10} {student.average_score():<15.2f}")

if __name__ == "__main__":
    main()


#Объяснение программы:
#Класс Student: Хранит информацию о студенте, включая фамилию, группу и результаты экзаменов. Метод average_score вычисляет средний балл студента.
#Функция main:
 #Запрашивает количество студентов и их данные.
 #Создает список объектов Student.
 #Фильтрует студентов с средним баллом не менее 4.
 #Сортирует отфильтрованных студентов по среднему баллу в порядке убывания.
 #Выводит результаты в виде таблицы.
