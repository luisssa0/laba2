import random

group1 = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Козлов", "Новиков", "Волков", "Зайцев", "Андреев"]
group2 = ["Соколов", "Михайлов", "Федоров", "Тихонов", "Белов", "Комаров", "Лебедев", "Макаров", "Сазонов", "Романов"]

team = random.sample(group1, 5) + random.sample(group2, 5)
team = tuple(team)

print("Группа 1:", group1)
print("Группа 2:", group2)
print("Команда:", team)

print("Длина команды:", len(team))

team = tuple(sorted(team))

if "Иванов" in team:
    print("Студент Иванов в команде!")
    count_ivanov = team.count("Иванов")
    print("Количество студентов Иванов в команде:", count_ivanov)
else:
    print("Студент Иванов не в команде!")
