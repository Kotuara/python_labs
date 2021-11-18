#Задания 25.1, 25.2, 25.4
import random
import string

def password_check(password, m):
    up = 0
    digit = 0
    for char in password:
        if char.isupper() == 1:
            up += 1
        if char.isdigit() == 1:
            digit += 1
    if up >= 1 and digit >= 1:
        print(password)
    else:
        generate_password(m)

def generate_password(m):
    alphabet = string.ascii_letters + string.digits
    prohibited = ['l', 'I', '1', 'o', 'O', '0']
    password = ''
    i = 0
    while i < m:
        char = random.choice(alphabet)
        if char not in prohibited:
            if char not in password:
                password += char
                i += 1
    password_check(password, m)

def main(n, m):
    for i in range(n):
        generate_password(m)

#Задание 25.3
def precise_pi(n):
    k = 0.0
    for i in range(n):
        x = random.random()
        y = random.random()
        k += (x * x + y * y < 1.0)
    print(4 * k / n)

#Задание 26.1
from PIL import Image, ImageDraw
def gradient(color):
    img = Image.new("RGB", (512, 200), (0, 0, 0))
    grad = ImageDraw.Draw(img)
    r = 0
    g = 0
    b = 0
    for i in range(img.size[0]):
            grad.line((i, 0, i, 512), fill=(r, g, b), width=2)
            if i % 4 == 0:
                if color == "R":
                    r += 2
                elif color == "G":
                    g += 2
                elif color == "B":
                    b += 2
                elif color == "V":
                    r += 2
                    b += 2
                elif color == "C":
                    g += 2
                    b += 2
                elif color == "Y":
                    r += 2
                    g += 2
                else:
                    r += 2
                    g += 2
                    b += 2
    img.save("Gradient.png", "PNG")

#Задание 26.2
def board(num, size):
    res = Image.new("RGB", (num * size, num * size), (255, 255, 255))
    chessboard = ImageDraw.Draw(res)
    x = 0
    y = 0
    for i in range(num):
        for j in range(num):
            if i % 2 == 0:
                if j % 2 == 0:
                    chessboard.rectangle((x, y, x + size, y + size), fill=("black"), width=1)
            if i % 2 == 1:
                if j % 2 == 1:
                    chessboard.rectangle((x, y, x + size, y + size), fill=("black"), width=1)
            x += size
        x = 0
        y += size
    res.save("res.png", "PNG")

#Задание 26.3
def makeanaglyph(filename, delta):
    img = Image.open(filename)
    x, y = img.size
    res = Image.new('RGB', (x, y), (0, 0, 0))
    pixels2 = res.load()
    pixels = img.load()
    for i in range(x):
        for j in range(y):
            if i < delta:
                r, g, b = pixels[i, j]
                pixels2[i, j] = 0, g, b
            else:
                pixels2[i, j] = r, g, b
                g, b = pixels[i, j][1:]
                r = pixels[i - delta, j][0]
        res.save("anaglyph.jpg")

#Задание 26.4
def cool_name():
    name = Image.new("RGB", (1100, 400), (255, 255, 255))
    cool = ImageDraw.Draw(name)
    cool.line((50, 50, 50, 350), fill=("red"), width = 10)
    cool.line((50, 200, 200, 50), fill=("red"), width = 10)
    cool.line((50, 200, 200, 350), fill=("red"), width = 10)
    cool.ellipse((230, 50, 430, 350), fill=("green"))
    cool.ellipse((270, 90, 390, 310), fill=("white"))
    cool.ellipse((460, 50, 660, 350), fill=("blue"))
    cool.ellipse((500, 90, 1000, 310), fill=("white"))
    cool.line((680, 50, 860, 50), fill=("red"), width = 10)
    cool.line((770, 50, 770, 350), fill=("red"), width = 10)
    cool.line((1030, 100, 1030, 350), fill=("red"), width = 10)
    cool.line((1030, 100, 900, 350), fill=("red"), width = 10)
    cool.ellipse((900, 50, 1050, 200), fill=("green"))
    cool.ellipse((930, 80, 1020, 170), fill=("white"))
    name.save("name.png", "PNG")

#Задание 27.1
def make_preview(size, n_colors):
    img = Image.open("kek.jpg")
    x, y = img.size
    res = Image.new('RGB', (size), (0, 0, 0))
    res = img.thumbnail(size)
    res = img.quantize(n_colors)
    res.save("res.bmp", "BMP")

#Задание 27.2
def image_filter():
    img = Image.open("kek.jpg")
    red, green, blue = img.split()
    new_img = Image.merge("RGB", (blue, green, red))
    new_img.save("filter.jpg", "JPEG")

while 1:
    exec(input())

