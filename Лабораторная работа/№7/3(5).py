class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.goals_scored = 0
        self.goals_conceded = 0

    def update_score(self, scored, conceded):
        self.goals_scored += scored
        self.goals_conceded += conceded
        if scored > conceded:
            self.points += 3  # Win
        elif scored == conceded:
            self.points += 1  # Draw

    def goal_difference(self):
        return self.goals_scored - self.goals_conceded


class League:
    def __init__(self):
        self.teams = {}

    def add_game(self, team1_name, team1_score, team2_name, team2_score):
        if team1_name not in self.teams:
            self.teams[team1_name] = Team(team1_name)
        if team2_name not in self.teams:
            self.teams[team2_name] = Team(team2_name)

        self.teams[team1_name].update_score(team1_score, team2_score)
        self.teams[team2_name].update_score(team2_score, team1_score)

    def get_standings(self):
        standings = sorted(self.teams.values(), key=lambda t: (-t.points, -t.goal_difference()))
        return standings


def print_standings(standings):
    print(f"{'Place':<5} {'Team':<20} {'Points':<6}")
    print("-" * 32)
    for place, team in enumerate(standings, start=1):
        print(f"{place:<5} {team.name:<20} {team.points:<6}")

# Пример использования
league = League()
league.add_game("Team A", 2, "Team B", 1)
league.add_game("Team C", 1, "Team D", 1)
league.add_game("Team A", 3, "Team C", 0)
league.add_game("Team B", 0, "Team D", 2)

standings = league.get_standings()
print_standings(standings)


#Объяснение программы:
#Класс Team: Хранит информацию о команде, включая название, очки, забитые и пропущенные голы. Метод update_score обновляет очки и статистику команды на основе результата игры.

#Класс League: Управляет командами и играми. Метод add_game добавляет результаты игры между двумя командами, обновляя их статистику. Метод get_standings возвращает отсортированный список команд по очкам и разнице забитых и пропущенных мячей.

#Функция print_standings: Выводит таблицу с местами команд, их названиями и количеством очков.

