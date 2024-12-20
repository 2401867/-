class Student:
    def __init__(self, name, grade, missed_classes):
        self.name = name
        self.grade = grade
        self.missed_classes = missed_classes

def get_failing_students(students):
    # Фильтруем студентов с оценкой "2"
    failing_students = [student for student in students if student.grade == 2]
    # Сортируем по количеству пропущенных занятий в порядке убывания
    failing_students.sort(key=lambda x: x.missed_classes, reverse=True)
    return failing_students

# Пример использования
students = [
    Student("Иванов", 2, 5),
    Student("Петров", 3, 2),
    Student("Сидоров", 2, 3),
    Student("Кузнецов", 5, 1),
]

failing_students = get_failing_students(students)

# Выводим список неуспевающих студентов
for student in failing_students:
    print(f"{student.name}: {student.missed_classes} пропущенных занятий")



#Объяснение:
#Класс Student: Определяет студента с именем, оценкой и количеством пропущенных занятий.
#Функция get_failing_students: Фильтрует студентов с оценкой "2" и сортирует их по количеству пропущенных занятий в порядке убывания.
#Пример использования: Создается список студентов, и выводится список неуспевающих студентов с указанием количества пропущенных занятий.
