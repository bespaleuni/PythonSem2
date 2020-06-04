from PIL import Image, ImageDraw, ImageFont
from os import listdir

image = Image.open(f'src/img.jpg')
qr = Image.open('src/qr.png')
logo = Image.open('src/logo.png')
out = f'out/img.png'
im_width = 1000;

assert im_width >= 480, RuntimeError("Small size")
im_height = im_width * image.size[1] // image.size[0]
image = image.resize((im_width, im_height), Image.ANTIALIAS)

"""lo_width = im_width // 10
lo_height = lo_width * logo.size[1] // logo.size[0]"""
logo = logo.resize((100, 100), Image.ANTIALIAS)

qr = qr.resize((100, 100), Image.ANTIALIAS)

if image.size[1] > image.size[0]:
    image = image.rotate(180)

draw = ImageDraw.Draw(image)
date = image.getexif().get(306).split()[0]
text = "Сяргей Кузьмянцоў"
font = ImageFont.truetype("arial.ttf", size=14)
draw.text((im_width // 2 - 125, im_height - 50), f"{text}\n{date}", font=font)

image.paste(logo, (im_width - 100, 0), logo)
image.paste(qr, (0, 0))
image.save(out)
