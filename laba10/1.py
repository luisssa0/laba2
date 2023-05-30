import json


json_file = '1.json'


with open(json_file, 'r') as file:
    data = json.load(file)


products = data['products']


for product in products:
    name = product['name']
    price = product['price']
    weight = product['weight']
    available = product['available']

    print("Название:", name)
    print("Цена:", price)
    print("Вес:", weight)
    if available:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()