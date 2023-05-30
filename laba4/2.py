def divide_100_by_number(number):
    try:
        result = 100 / number
        return result
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    except ValueError:
        print("Ошибка: введено некорректное значение!")


user_input = input("Введите число для деления 100: ")

try:
    number = int(user_input)
    result = divide_100_by_number(number)
    if result is not None:
        print(f"Результат деления 100 на {number}: {result}")
except ValueError:
    print("Ошибка: введено некорректное значение!")
