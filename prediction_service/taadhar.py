#!/usr/bin/env python
import sys
import pytesseract
import re
from PIL import Image

def get_text(path):
    img = Image.open(path)
    img = img.convert('RGBA')
    pix = img.load()

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
                pix[x, y] = (0, 0, 0, 255)
            else:
                pix[x, y] = (255, 255, 255, 255)

    img.save('temp.png')

    text = pytesseract.image_to_string(Image.open('temp.png'))

    # Initializing data variable
    name = None
    contact = None
    rci = None

    lines = text

    for line in lines.split('\n'):
        wordlist = line.split()
        if [word for word in wordlist if re.search('Name', word)]:
            nameline = line
            break

    name = nameline.split(":")[1].strip()

    lines = text

    for line in lines.split('\n'):
        wordlist = line.split()
        if [word for word in wordlist if re.search('Contact', word)]:
            contactline = line
            break

    contact = contactline.split(":")[1].strip()

    lines = text

    for line in lines.split('\n'):
        wordlist = line.split()
        if [word for word in wordlist if re.search('RCI', word)]:
            rciline = line
            break

    rci = rciline.split(":")[1].strip()

    return name, contact, rci

def get_rough_text(path = "Unknown.jpeg"):
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    print(text)

if __name__ == "__main__":
    get_rough_text()


#G. Anupama
#9441496091