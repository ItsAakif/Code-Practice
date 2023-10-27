from PIL import Image, ImageFilter
im=Image.open(’1.jpg’)
im=im.filter(ImageFilter.GaussianBlur(10))
im.show()
