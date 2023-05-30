from PIL import Image
water = "ba.png"

with Image.open (water) as img_water:
   img_water.load()

img_water = Image.open(water)
img_water = img_water.resize((img_water.width // 10, img_water. height // 10))
filename ="1.jpg"
with Image. open (filename) as img:
   img.load ()
img.paste(img_water, (42, 50), img_water)
img.save ("watermark.png")
img.show()