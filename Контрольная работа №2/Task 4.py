''' 4. Лыжные гонки проводятся отдельно для двух групп участников. Результаты соревнований заданы в виде фамилий участников и их результатов в каждой группе. Расположить результаты соревнований в каждой группе в порядке занятых мест. Объединить результаты обеих групп с сохранением упорядоченности и вывести в виде таблицы с заголовком.'''


class Participant:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class SkiRace:
    def __init__(self):
        self.group_a = []
        self.group_b = []

    def add_participant(self, group, name, score):
        participant = Participant(name, score)
        if group == 'A':
            self.group_a.append(participant)
        elif group == 'B':
            self.group_b.append(participant)

    def sort_participants(self, participants):
        # Сортировка участников по результатам (сортировка пузырьком)
        n = len(participants)
        for i in range(n):
            for j in range(0, n-i-1):
                if participants[j].score > participants[j+1].score:
                    participants[j], participants[j+1] = participants[j+1], participants[j]

    def display_results(self):
        self.sort_participants(self.group_a)
        self.sort_participants(self.group_b)

        print(f"{'Name':<20} {'Score':<10}")
        print("-" * 30)

        for participant in self.group_a:
            print(f"{participant.name:<20} {participant.score:<10}")

        for participant in self.group_b:
            print(f"{participant.name:<20} {participant.score:<10}")

# Пример использования
race = SkiRace()
race.add_participant('A', 'Иванов', 85)
race.add_participant('A', 'Петров', 90)
race.add_participant('B', 'Сидоров', 78)
race.add_participant('B', 'Кузнецов', 88)

race.display_results()
