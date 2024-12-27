''' 2. Соревнования по футболу между командами проводятся в два этапа. Для проведения первого этапа участники разбиваются на две группы по 12 команд. Для проведения второго этапа выбирается 6 лучших команд каждой группы по результатам первого этапа. Составить список команд участников второго этапа.'''

class Team:
    def __init__(self, name, points):
        self.name = name
        self.points = points

class Tournament:
    def __init__(self):
        self.group_a = []
        self.group_b = []

    def add_team(self, group, team):
        if group == 'A':
            self.group_a.append(team)
        elif group == 'B':
            self.group_b.append(team)

    def get_top_teams(self, group, top_n):
        if group == 'A':
            teams = self.group_a
        elif group == 'B':
            teams = self.group_b
        else:
            return []

        # Сортировка команд по очкам без использования встроенной сортировки
        for i in range(len(teams)):
            for j in range(len(teams) - 1):
                if teams[j].points < teams[j + 1].points:
                    teams[j], teams[j + 1] = teams[j + 1], teams[j]

        return teams[:top_n]

# Пример использования
tournament = Tournament()

# Добавление команд в группы
tournament.add_team('A', Team('Team A1', 30))
tournament.add_team('A', Team('Team A2', 25))
tournament.add_team('A', Team('Team A3', 20))
tournament.add_team('A', Team('Team A4', 15))
tournament.add_team('A', Team('Team A5', 10))
tournament.add_team('A', Team('Team A6', 5))
tournament.add_team('A', Team('Team A7', 35))
tournament.add_team('A', Team('Team A8', 40))
tournament.add_team('A', Team('Team A9', 45))
tournament.add_team('A', Team('Team A10', 50))
tournament.add_team('A', Team('Team A11', 55))
tournament.add_team('A', Team('Team A12', 60))

tournament.add_team('B', Team('Team B1', 30))
tournament.add_team('B', Team('Team B2', 25))
tournament.add_team('B', Team('Team B3', 20))
tournament.add_team('B', Team('B4', 15))
tournament.add_team('B', Team('B5', 10))
tournament.add_team('B', Team('B6', 5))
tournament.add_team('B', Team('B7', 35))
tournament.add_team('B', Team('B8', 40))
tournament.add_team('B', Team('B9', 45))
tournament.add_team('B', Team('B10', 50))
tournament.add_team('B', Team('B11', 55))
tournament.add_team('B', Team('B12', 60))

# Получение лучших команд для второго этапа
top_teams_a = tournament.get_top_teams('A', 6)
top_teams_b = tournament.get_top_teams('B', 6)

# Вывод результатов
print("Команды второго этапа:")
for team in top_teams_a + top_teams_b:
    print(f"{team.name} - {team.points} очков")
