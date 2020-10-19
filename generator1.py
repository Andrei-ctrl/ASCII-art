from PIL import Image, ImageFont

import math

"""ASCII_CHARS = "#?%.S+.*:,@"""
ASCII_CHARS = 'W@S#?%+*o:-,. '[::-1]
charArray = list(ASCII_CHARS)
charLenght = len(charArray)
interval = charLenght/256

ScaleFactor = 0.1

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

text_file = open("jjjj1.txt", "w")

im = Image.open("ferarri.jpg")

fnt = ImageFont.truetype('C:\Windows\Fonts\\lucon.ttf', 7)

width, height = im.size
im = im.resize((int(ScaleFactor*width), int(ScaleFactor*height*(8/18))), Image.NEAREST)
width, height = im.size
pix = im.load()

outputImage = Image.new('RGB', (8 * width, 18 * height), color = (0, 0, 0))


for i in range(height):
    for j in range(width):
            r, g, b = pix[j, i]
            h = int(r / 3 + g / 3 + b / 3)
            pix[j, i] = (h, h, h)
            text_file.write(getChar(h))

    text_file.write('\n')

im.save("output.png")




