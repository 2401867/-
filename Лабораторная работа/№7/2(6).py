''' 6. Протокол соревнований по прыжкам в воду содержит список фамилий спортсменов и баллы, выставленные 5 судьями по результатам 2 прыжков. Получить итоговый протокол, содержащий фамилии и результаты, в порядке занятых спортсменами мест по результатам 2 прыжков. '''

class Diver:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def total_score(self):
        return sum(self.scores)

class Competition:
    def __init__(self):
        self.divers = []

    def add_diver(self, name, scores):
        self.divers.append(Diver(name, scores))

    def sort_divers(self):
        # Реализация сортировки пузырьком
        n = len(self.divers)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.divers[j].total_score() < self.divers[j+1].total_score():
                    self.divers[j], self.divers[j+1] = self.divers[j+1], self.divers[j]

    def display_results(self):
        self.sort_divers()
        print("Итоговый протокол:")
        for i, diver in enumerate(self.divers, start=1):
            print(f"{i}. {diver.name}: {diver.total_score()}")

# Пример использования
competition = Competition()
competition.add_diver("Иванов", [8.5, 9.0, 8.0, 9.5, 8.5])
competition.add_diver("Петров", [9.0, 9.5, 9.0, 9.0, 9.0])
competition.add_diver("Сидоров", [7.5, 8.0, 8.5, 7.0, 8.0])

competition.display_results()
