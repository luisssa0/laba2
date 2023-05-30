from PIL import Image


img = Image.open("example.jpg")


width, height = img.size


new_size = (int(width/3), int(height/3))
small_img = img.resize(new_size)
small_img.save("small_example.jpg")


mirror_img_h = img.transpose(Image.FLIP_LEFT_RIGHT)
mirror_img_v = img.transpose(Image.FLIP_TOP_BOTTOM)


mirror_img_h.save("mirror_horizontal.jpg")
mirror_img_v.save("mirror_vertical.jpg")
