from PIL import Image


cards = {
    "День рождения": "birthday_card.jpg",
    "Новый год": "new_year_card.jpg",
    "День святого Валентина": "valentine_card.jpg",
    "8 марта": "womens_day_card.jpg"
}


holiday = input("К какому празднику вы ищете открытку? ")
file=cards[holiday]
with Image.open(file) as img:
    img.load()
img.show()