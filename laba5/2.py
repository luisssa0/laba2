my_list = [1, 2, 3, 4, 5, 3, 2]
unique_list = set(my_list)
if len(unique_list) < len(my_list):
    print("Список содержит повторяющиеся элементы.")
    for item in unique_list:
        if my_list.count(item) > 1:
            print(f"Повторяющийся элемент: {item}")
else:
    print("Список не содержит повторяющихся элементов.")
