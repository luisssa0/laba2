from PIL import Image


im = Image.open("example.jpg")


left = 100
top = 100
right = 500
bottom = 500


im_crop = im.crop((left, top, right, bottom))


im_crop.save("print_crop.jpg")
