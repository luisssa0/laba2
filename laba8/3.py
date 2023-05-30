from PIL import Image, ImageDraw, ImageFont


card_dict = {
    "День рождения": "birthday.jpg",
}


holiday = input("Введите название праздника: ")


if holiday in card_dict:

    filename = card_dict[holiday]

    image = Image.open("birthday_card.jpg")

    cropped_image = image.crop((100, 100, 500, 500))

    name = input("Введите имя того, кого хотите поздравить: ")

    draw = ImageDraw.Draw(cropped_image)
    text = f"{name}, поздравляю!"
    font = ImageFont.truetype("arial.ttf", size=30)
    draw.text((100, 20), text, font=font, fill="red")

    cropped_image.save("new_card.png")
    print("Новая открытка сохранена.")
else:
    print("Извините, такого праздника нет в списке.")
