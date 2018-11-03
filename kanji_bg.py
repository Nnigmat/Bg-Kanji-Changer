from PIL import Image, ImageFont, ImageDraw

def draw(kanji, path_bg='wallpaper.png', path_font='', font_color=(239, 240, 240)):
    image = Image.open(fp=path_bg)
    font = ImageFont.truetype(font=path_font, size=250)

    draw = ImageDraw.Draw(image)

    draw.text(xy=position, text=text, fill=font_color, font=font)


