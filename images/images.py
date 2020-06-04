from PIL import Image, ImageDraw, ImageFont
from os import listdir

image = Image.open(f'src/img.jpg').convert('RGBA')
qr = Image.open('src/qr.png').convert('RGBA')
logo = Image.open('src/logo.png').convert('RGBA')
out = f'out/img.png'
width = 1000;

assert width >= 480, RuntimeError("Small size")
height = width * image.size[1] // image.size[0]
image = image.resize((width, height), Image.ANTIALIAS)
logo = logo.resize((100, 100), Image.ANTIALIAS)
qr = qr.resize((100, 100), Image.ANTIALIAS)

if image.size[1] > image.size[0]:
    image = image.rotate(180)

draw = ImageDraw.Draw(image)
date = image.getexif().get(306).split()[0]
text = "Сяргей Кузьмянцоў"
font = ImageFont.truetype("arial.ttf", size=14)
draw.text((width // 2 - 125, height - 50), f"{text}\n{date}", font=font)

image.paste(logo, (width - 100, 0), logo)
image.paste(qr, (0, 0))
image.save(out)
