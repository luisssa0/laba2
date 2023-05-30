
countries_capitals = {
    'Россия': 'Москва',
    'США': 'Вашингтон',
    'Франция': 'Париж',
    'Германия': 'Берлин',
    'Япония': 'Токио'
}


print("Все страны и столицы:")
for country, capital in countries_capitals.items():
    print(country + " - " + capital)


country = input("Введите страну: ")
if country in countries_capitals:
    print("Столица " + country + " - " + countries_capitals[country])
else:
    print("Такой страны нет в списке")


print("Страны и столицы в алфавитном порядке:")
for country in sorted(countries_capitals.keys()):
    print(country + " - " + countries_capitals[country])