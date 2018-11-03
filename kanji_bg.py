from PIL import Image, ImageFont, ImageDraw
from os import system

def draw(kanji, path_bg='src/wallpaper.png', path_font='', font_color=(239, 240, 240)):
    image = Image.open(fp=path_bg)

    draw = ImageDraw.Draw(image)

    # Position and text of kanji
    position = (3000, 1700)
    text = kanji[0]
    font = ImageFont.truetype(font=path_font, size=650)
    draw.text(xy=position, text=text, fill=font_color, font=font)

    if kanji[0] != kanji[1]:
        # Position and text of furigana
        position = (3100, 2500)
        text = kanji[1]
        font = ImageFont.truetype(font=path_font, size=200)
        draw.text(xy=position, text=text, fill=font_color, font=font)

    # Position and text of meaning
    position = (3200, 2800)
    text = kanji[3]
    font = ImageFont.truetype(font=path_font, size=150)
    draw.text(xy=position, text=text, fill=font_color, font=font)


    image.save('src/temp_wallpaper.png')
    system('feh --bg-scale src/temp_wallpaper.png')


