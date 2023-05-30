from PIL import Image


img = Image.open('example.jpg')


img.show()


width, height = img.size
print("Размер изображения: {}x{}".format(width, height))


print("Формат файла: {}".format(img.format))


print("Цветовая модель: {}".format(img.mode))
