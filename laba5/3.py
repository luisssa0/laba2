weekdays = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

x = int(input("Сколько выходных дней вы хотите на этой неделе? "))

if x == 1:
    weekends = weekdays[-1]
elif x > 1:
    weekends = weekdays[-x:]

workdays = weekdays[0:7-x]

print('Ваши выходные дни: ', *weekends)
print('Ваши рабочие дни: ', *workdays)