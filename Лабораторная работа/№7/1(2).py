class Participant:
    def __init__(self, surname, group, instructor, result):
        self.surname = surname
        self.group = group
        self.instructor = instructor
        self.result = result

    def meets_standard(self, standard):
        return self.result <= standard


class CrossResults:
    def __init__(self):
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def sort_results(self):
        self.participants.sort(key=lambda x: x.result)

    def count_meeting_standard(self, standard):
        return sum(1 for p in self.participants if p.meets_standard(standard))

    def display_results(self):
        print(f"{'Surname':<20} {'Group':<10} {'Instructor':<20} {'Result':<10} {'Meets Standard'}")
        for p in self.participants:
            meets_standard = "Yes" if p.meets_standard(standard) else "No"
            print(f"{p.surname:<20} {p.group:<10} {p.instructor:<20} {p.result:<10} {meets_standard}")


# Ввод данных
standard = 2.0  # Норматив (например, 2 минуты)
results = CrossResults()

num_participants = int(input("Введите количество участниц: "))
for _ in range(num_participants):
    surname = input("Введите фамилию: ")
    group = input("Введите группу: ")
    instructor = input("Введите фамилию преподавателя: ")
    result = float(input("Введите результат (в минутах): "))
    participant = Participant(surname, group, instructor, result)
    results.add_participant(participant)

# Сортировка и вывод результатов
results.sort_results()
results.display_results()

# Подсчет участниц, выполнивших норматив
count = results.count_meeting_standard(standard)
print(f"\nКоличество участниц, выполнивших норматив: {count}")


#Объяснение программы:
#Класс Participant: Хранит информацию о каждой участнице, включая фамилию, группу, фамилию преподавателя и результат. Метод meets_standard проверяет, выполнила ли участница норматив.

#Класс CrossResults: Хранит список участниц и предоставляет методы для добавления участниц, сортировки результатов, подсчета участниц, выполнивших норматив, и отображения результатов.

#Ввод данных: Программа запрашивает у пользователя количество участниц и их данные.

#Сортировка и вывод: Результаты сортируются по времени, и выводится таблица с информацией о каждой участнице.

#Подсчет нормативов: В конце программа выводит количество участниц, выполнивших норматив.
