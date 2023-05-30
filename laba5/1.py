numbers = [5, 10, 15, 20, 25]

user_number = input("Введите число: ")
user_number = int(user_number)

if user_number in numbers:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")

print("Исходный список:", numbers)
print("Число пользователя:", user_number)
