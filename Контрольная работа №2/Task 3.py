''' 1. Результаты сессии содержат оценки 5 экзаменов по каждой группе. Определить средний балл для трех групп студентов одного потока и выдать список групп в порядке убывания среднего балла. Результаты вывести в виде таблицы с заголовком.'''


class Group:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average_score(self):
        return sum(self.scores) / len(self.scores)


class SessionResults:
    def __init__(self):
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)

    def display_results(self):
        # Сортируем группы по среднему баллу в порядке убывания
        sorted_groups = sorted(self.groups, key=lambda g: g.average_score(), reverse=True)

        # Выводим заголовок таблицы
        print(f"{'Группа':<20} {'Средний балл':<15}")
        print("-" * 35)

        # Выводим результаты
        for group in sorted_groups:
            print(f"{group.name:<20} {group.average_score():<15.2f}")


# Пример использования
if __name__ == "__main__":
    results = SessionResults()

    # Добавляем группы и их оценки
    results.add_group(Group("Группа A", [4, 5, 3, 4, 5]))
    results.add_group(Group("Группа B", [2, 3, 4, 3, 2]))
    results.add_group(Group("Группа C", [5, 5, 4, 5, 5]))

    # Отображаем результаты
    results.display_results()



#Объяснение:
#Класс Group: представляет группу студентов и их оценки. Метод average_score вычисляет средний балл группы.
#Класс SessionResults: управляет списком групп и выводит результаты. Метод display_results сортирует группы по среднему баллу и выводит их в виде таблицы.
#Пример использования: создается объект SessionResults, добавляются группы с их оценками, и затем результаты выводятся на экран.
