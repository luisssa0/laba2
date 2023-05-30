from PIL import Image, ImageFilter
from pathlib import Path


current_dir = Path.cwd()
filenames = Path(current_dir).glob('*')
Path('new_dir').mkdir(parents=True, exist_ok=True)
for file in ("1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"):
    with Image.open(file) as img:
        img.load()
        new_img = img.filter(ImageFilter.CONTOUR)
        new_img.save(Path("new_dir/new_" + str(file)))
