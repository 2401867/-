class Team:
    def __init__(self, name):
        self.name = name
        self.scores = 0

    def add_score(self, score):
        self.scores += score


class Competition:
    def __init__(self):
        self.teams = {
            'Team A': Team('Team A'),
            'Team B': Team('Team B'),
            'Team C': Team('Team C')
        }

    def calculate_scores(self, results):
        for position, team_name in enumerate(results):
            score = self.get_score(position + 1)
            self.teams[team_name].add_score(score)

    @staticmethod
    def get_score(position):
        if position == 1:
            return 5
        elif position == 2:
            return 4
        elif position == 3:
            return 3
        elif position == 4:
            return 2
        elif position == 5:
            return 1
        return 0

    def get_winner(self):
        winner = max(self.teams.values(), key=lambda team: (team.scores, -results.index(team.name)))
        return winner.name, winner.scores


# Пример использования
results = ['Team A', 'Team B', 'Team C', 'Team A', 'Team B', 'Team C', 
           'Team A', 'Team B', 'Team C', 'Team A', 'Team B', 'Team C', 
           'Team A', 'Team B', 'Team C', 'Team A', 'Team B', 'Team C']

competition = Competition()
competition.calculate_scores(results)
winner_name, winner_score = competition.get_winner()

print(f"Победитель: {winner_name} с {winner_score} баллами.")


#Объяснение:
#Класс Team: Хранит имя команды и её баллы.
#Класс Competition: Управляет командами и подсчитывает баллы на основе результатов.
#Метод calculate_scores: Принимает список результатов и начисляет баллы командам.
#Метод get_winner: Определяет победителя на основе набранных баллов.
