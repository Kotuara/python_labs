#Задание 18.1
def print_shrug_smile():
    print('¯\_(ツ)_/¯ ')
def print_ktulhu_smile():
    print('{:€')
def print_happy_smile():
    print('(͡° ͜ʖ ͡°)')

#Задание 18.2
def ask_password():
    string = 'password'
    i = 0
    while i < 3:
        word = input()
        if word != string:
            if i == 2:
                print('В доступе отказано')
        elif word == string:
            print('Пароль принят')
            break
        i += 1

#Задание 18.3
def golden_ratio(i):
    fibonacсi = [1,1,2,3,5,8,13,21,34,55]
    if i >= 9:
        for n in range(8, i):
            fibonacсi.append(fibonacсi[n-2] + fibonacсi[n-1])
            n += 1
    print(fibonacсi[i+1] / fibonacсi[i])

#Задание 18.4
def bracket_check(test_string):
    while (len(test_string) != 0) or (len(set(test_string)) > 1):
        test_string = test_string.replace('()','')
        if len(set(test_string)) == 1 or test_string == ')(':
            print("NO")
            break
    else: print("YES")

#Задание 18.5
def equation(a,b):
    x1, y1, x2, y2 = map(float, (a + ";" + b).replace(',', '.').split(';'))
    if x1 == x2:
        print(x1)
    elif y1 == y2:
            print(y1)
    else:
        k = (y2 - y1)  /  (x2 - x1)
        print(k, y2 - k * x2)

#Задание 18.6
def line(s,t):
    k, b = map(float, s.replace('x', ' ').split(' '))
    x, y = map(float, (t).split(';'))
    if y == k * x + b:
        print("True")
    else:
        print("False")

#Задание 19.1
def month_name(n, str):
    year = ['january','february','march','april','may','june','july','august','september','october','november','december']
    god = ['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
    if str == "en":
        return (year[n-1])
    elif str == "ru":
        return (god[n-1])

#Задание 19.2
def t2c(f):
    a=f[:1]
    b=f[1:]
    r=int(b)
    c='ABCDEFGH'.find(a)+1
    return (c,r)

def c2t(k):
    (c,r)=k
    return 'ABCDEFGH'[c-1]+str(r)

def possible_turns(cell):
    (c,r)=t2c(cell)
    tmp=[]
    tmp.append((c+2,r+1))
    tmp.append((c+2,r-1))
    tmp.append((c-2,r+1))
    tmp.append((c-2,r-1))
    tmp.append((c+1,r+2))
    tmp.append((c-1,r+2))
    tmp.append((c+1,r-2))
    tmp.append((c-1,r-2))
    res=[]
    for ((a,b)) in tmp:
        if (a>0) & (b>0) & (a<=8) & (b<=8):
            res+=[c2t((a,b))]
    return sorted(res)

#Задание 19.3
def roots_of_quadratic_equation(a,b,c):
    result = []
    if a == 0 and b == 0 and c == 0:
        result.append("all")
        return result
    elif a == 0 and b == 0:
        return []
    elif c == 0:
        result.append(0)
        result.append((-1 * b) // a)
        return result
    elif a == 0:
        result.append(-c / b)
    else:
        d = b ** 2 - 4 * a * c
        if d > 0:
            result.append((-b + d // d) // 2 * a)
            result.append((-b - d // d) // 2 * a)
        if d == 0:
            result.append(-b // 2 * a)
    return result

#Задание 19.4
def palindrome(s):
    s = s.lower().replace(' ','')
    if s == s[::-1]:
        return ("Палиндром")
    else:
        return ("Не палиндром")

#Задание 19.5
def prime(number):
    counter = 0
    if number == 1:
        return ("Ни простое ни составное")
    else:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                counter += 1
        if counter > 0:
            return ("Составное число")
        else:
            return ("Простое число")

#Задание 19.6
def catalan(n):
    c = [0] * (n + 1)
    c[0] = 1
    for k in range(1, n + 1):
        c[k] = sum(c[i] * c[k - i - 1] for i in range(k))
    return c[n]

#Задание 20.1
def translate(text):
    vowel = ['А', 'О', 'Э', 'Е', 'И', 'Ы', 'У', 'Ё', 'Ю', 'Я',
             'а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я',
             ',', '.', '!', '?', '-']
    for x in text:
        if x in vowel:
            text = text.replace(x, '')
    print('translatedText == "' + ' '.join(text.split()) + '"')

#Задание 20.2
def setup_profile(name, vacationDates):
    global Name
    Name = name
    global Date
    Date = vacationDates

def print_application_for_leave():
    print("Заявление на отпуск в период", Date, ".")

def print_holiday_money_claim(amount):
    print("Прошу выплатить", amount, "отпускных денег.")

def print_attorney_letter(toWhom):
    print("На время отпуска в период", Date, "моим заместителем назначается", toWhom, ".", Name)

#Задание 20.3
messages = []
def print_only_new(message):
    if message not in messages:
        messages.append(message)
        print(message)

#Задание 20.4
base = []
def hello(name):
    print("Здравствуйте,", name, "! Вашу карту ищут...")

def search_card(name):
    if name in base:
        print("Ваша карта с номером", base.index(name)+1 , "найдена")
    else:
        print("Ваша карта не найдена")

#Задание 20.5
lastTicket = 0
def luckiness(c):
    a = c % 1000
    b = c // 1000
    if a % 10 + a // 10 % 10 + a // 100 == b % 10 + b // 10 % 10 + b // 100:
        return True

def lucky(ticket):
    tick = ''
    if len(str(ticket)) != 6:
       tick = '0' * (6 - len(str(ticket))) + str(ticket)
    print(tick)
    if luckiness(lastTicket) == luckiness(ticket) == True:
        return ("Счастливый")
    else:
        return ("Несчастливый")

#Задание 20.6
bets = []
def do_bet(horse, bet):
    if horse not in bets and bet > 0:
        bets.append(horse)
        print("Ваша ставка в размере", bet, "на лошадь", horse, "принята")
    else:
        print("Что-то пошло не так, попробуйте снова")

#Задание 21.1
a = []
def from_string_to_list(string, container):
    container.append(' '.join(string.split()))

#Задание 21.2
matrix = [[]]
def transpose(matrix):
    res=[]
    n=len(matrix)
    m=len(matrix[0])
    for j in range(m):
        tmp=[]
        for i in range(n):
            tmp=tmp+[matrix[i][j]]
        res=res+[tmp]
    matrix[:] = res
    return matrix

#Задание 21.3
first_content = []
second_content = []
def swap(first, second):
    first[:], second[:] = second[:], first[:]

#Задание 21.4
def defractalize(fractal):
    while fractal in fractal:
        fractal.remove(fractal)

#Задание 21.5
def fractal_print(obj):
    print('[' + ', '.join(map(str, obj)) + ']')

#Задание 21.6
wb_tree = []
def tree():
    white = []
    black = [white, white, white]
    white.append(black)
    white.append(black)
    wb_tree = black

#Задание 22.1
shift = 3
signs = [' ', ',', '.', '!', '?']
def encrypt_caesar(msg, shift):
    message = ''
    for i in range(len(msg)):
        if msg[i] in signs:
            message += msg[i]
        else:
            k = ord(msg[i])
            l = k + shift
            message += ' '.join(chr(l))
    return message

def decrypt_caesar(msg, shift):
    message = ''
    for i in range(len(msg)):
        if msg[i] in signs:
            message += msg[i]
        else:
            k = ord(msg[i])
            l = k - shift
            message += ' '.join(chr(l))
    return message

#Задание 22.2
def partial_sums(*args):
    sums = [0]
    for i,x in enumerate(args):
            sums.append(x + sums[i])
    return sums

#Задание 22.3
def score(first, second=0):
    scoring = {'Яблочко': 50, 'Зеленое_кольцо': 25,
           'Внешнее_кольцо': {1: 8, 2: 6, 3: 42, 20: 50},
           'Внутреннее_кольцо': {1: 2, 2: 16, 3: 56, 20: 3}}
    if second == 0:
        return scoring[first]
    else:
        return scoring[first][second]

#Задание 22.4
def solve(*coefficients):
    if len(coefficients) == 3:
        a, b, c = coefficients[0], coefficients[1], coefficients[2]
        return roots_of_quadratic_equation(a, b, c)
    elif len(coefficients) == 2:
        b, c = coefficients[0], coefficients[1]
        return -c / b
    elif len(coefficients) == 1:
        return 0
    else:
        return None

#Задание 22.5
a = input().split(' ')
for t, i in enumerate(a):
    a[t] = int(i)
def solve(a):
    if len(a) == 3:
        d = a[1] ** 2 - 4 * a[0] * a[2]
        if a[0] == 0 and a[1] == 0 and a[2] == 0:
            x = ["all"]
        elif a[0] == 0 and a[1] == 0:
            x = ''
        elif a[0] == 0:
            x = [-a[2] / a[1]]
        elif a[1] == 0:
            x = [(a[2] // a[0]) ** 0.5]
        elif a[2] == 0:
            x = [0, -a[1] // a[0]]
        else:
            if d == 0:
                x = [-a[1] // (2 * a[0])]
            elif d < 0:
                x = ''
            else:
                x = [int((-a[1] + d ** 0.5) // (2 * a[0])),
                     int((-a[1] - d ** 0.5) // (2 * a[0]))]
        return x
    elif len(a) == 2:
        return [-a[1] / a[0]]
    elif len(a) == 1:
        if a[0] == 0:
            return ["all"]
        else:
            return []
    else:
        return ["all"]

#Задание 23.1
transformation = lambda x: x

#Задание 23.2
def find_farthest_orbit(list_of_orbits):
    list = []
    for i in list_of_orbits:
        if i[0] != i[1]:
            list.append(i[0] * i[1])
    far = list.index(max(list))
    return list_of_orbits[far]

#Задание 23.3
def pam_param():
    text = input()
    vowel = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
    pam = text.split()
    rhymes = [0] * len(pam)
    for i in range(len(pam)):
        for x in pam[i]:
            if x in vowel:
                rhymes[i] += 1
    if len(set(rhymes)) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")

#Задание 23.4
import math
def astroids():
    def drange(start, stop, step):
         r = start
         while r < stop:
             yield r
             r += step
    def distance(t):
        return math.hypot(0.75 - t[0], 0 - t[1])
    coords =[(math.cos(3 * t), math.sin(3 * t)) for t in drange(0, 2*3.14, 0.1)]
    dists = [round(distance(x),4) for x in coords]
    print(min(dists))

#Задание 23.5
def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) < 2

#Задание 24.1
def is_zero_there():
    list = []
    while True:
        word = input()
        if word == '':
            break
        list.append(word)
    print(any([x == 0 for x in list]))

#Задание 24.2
def gematria():
    list = []
    while True:
        word = input()
        if word == '':
            break
        list.append(word)
    print(*sorted(list, key=lambda x: (sum([ord(i) - ord('A') + 1 for i in x.upper()]), x)), sep="\n")

#Задание 24.3
import sys
def comments():
    data = list(map(str.strip, sys.stdin))
    data = [s.strip() for s in data]
    coment = list(filter(lambda word: word[0] == '#', data))
    for e in coment:
        print(f'Line {data.index(e) + 1}: {e[1:].strip()}')

#Задание 24.4
def anagramm():
    list = []
    n = int(input())
    for i in range(n):
        list.append(input().lower())
    print(*sorted(list, key=lambda x: (sum([ord(i) for i in x]))), sep="\n")

while 1:
    exec(input())
