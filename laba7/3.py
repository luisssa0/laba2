
from PIL import Image,ImageFilter
for file in ("1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"):
    with Image.open(file) as img:
        img.load()
        one_img = img.filter(ImageFilter.CONTOUR)
        one_img.save("new1.jpg")
        one_img.show()
        two_img= img.filter(ImageFilter.EMBOSS)
        two_img.save("new2.jpg")
        two_img.show()
        three_img=img.filter(ImageFilter.EDGE_ENHANCE)
        three_img.save("new3.jpg")
        three_img.show()







