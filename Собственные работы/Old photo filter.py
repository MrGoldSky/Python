from PIL import Image, ImageFilter
from math import ceil 

# n - степень размытия
# filename - изображение
# s - степень накладываемой остроты ( в % )
# save_name - название файла для сохранения

# Функция накладывает на изображение фильтр старых фото


def old_style_photo(file_name, save_name="save.jpg", n=0.6, s=20):
    im = Image.open(file_name)
    newImage = im.filter(ImageFilter.UnsharpMask(radius=2, percent=s))
    newImage = newImage.filter(ImageFilter.GaussianBlur(radius=n))
    pixels = newImage.load()
    x, y = newImage.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            rr = ceil(max(0, min(255, 0.393 * r + 0.769 * g + 0.189 * b)))
            gg = ceil(max(0, min(255, 0.349 * r + 0.686 * g + 0.168 * b)))
            bb = ceil(max(0, min(255, 0.272 * r + 0.534 * g + 0.131 * b)))
            pixels[i, j] = rr, gg, bb
    newImage.save(save_name)

old_style_photo("image.jpg", "save.jpg", 0.6, 20)

