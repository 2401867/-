class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_result(self, result):
        if result == 'win':
            self.points += 1
        elif result == 'draw':
            self.points += 0.5
        elif result == 'loss':
            self.points += 0

    def __repr__(self):
        return f"{self.name}: {self.points} points"


def main():
    players = []
    num_players = int(input("Введите количество участников: "))

    for _ in range(num_players):
        name = input("Введите фамилию участника: ")
        players.append(Player(name))

    num_matches = int(input("Введите количество сыгранных партий: "))

    for _ in range(num_matches):
        player1_name = input("Введите фамилию первого участника: ")
        player2_name = input("Введите фамилию второго участника: ")
        result = input("Введите результат (win, draw, loss) для первого участника: ")

        # Обновляем очки участников
        for player in players:
            if player.name == player1_name:
                player.add_result(result)
            elif player.name == player2_name:
                if result == 'win':
                    player.add_result('loss')
                elif result == 'draw':
                    player.add_result('draw')

    # Сортируем игроков по очкам
    players.sort(key=lambda x: x.points, reverse=True)

    # Выводим итоговую таблицу
    print("\nИтоговая таблица:")
    for player in players:
        print(player)


if __name__ == "__main__":
    main()



#Объяснение:
#Класс Player: Хранит имя участника и количество очков. Метод add_result обновляет очки в зависимости от результата партии.
#Функция main: Запрашивает количество участников и их фамилии, затем количество сыгранных партий и результаты. Обновляет очки участников на основе введенных данных.
#Сортировка: Участники сортируются по очкам в порядке убывания.
#Вывод: Итоговая таблица выводится на экран.
