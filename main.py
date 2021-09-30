import random
import time


def horoskope():  # Задание 1.1
    print('Введите ваше имя, фамилию, любимое животное и знак зодиака:')
    name = input().capitalize()
    surname = input().capitalize()
    animal = input()
    zodiac = input()
    print('Индивидуальный гороскоп для пользователя ' + name + ' ' + surname +
          '\nКем вы были в прошлой жизни: ' + animal +
          '\nВаш знак зодиака - ' + zodiac + ' , поэтому вы - тонко чувствующая натура')


def bit_ne_bit():  # Задание 1.2
    print('1 бит - минимальная единица количества информации.'
          '\n1 байт = 8 бит.'
          '\n1 Килобит = 1024 бита.'
          '\n1 Килобайт = 1024 байта.'
          '\n1 Килобайт = ' + str(8 * 1024) + ' бит.')


def backward_parrot():  # Задание 1.3
    first = input()
    second = input()
    third = input()
    print(third + '\n' + second + '\n' + first)


def quest():  # Задание 2.1
    print('Вы просыпаетесь в тёмном и прохладном помещении, отовсюду веют сквозняки'
          '\nНепонятно, как вы здесь оказались, как отсюда выбраться, и есть ли здесь кто-то ещё'
          '\nРезко включившийся свет сильно бьёт по глазам и ослепляет вас'
          '\nНемного привыкнув к яркости, и снова открыв глаза, вы замечаете перед собой три двери с разными знаками: '
          '\nШпиль, ракушка и костер'
          '\nВидимо, делать больше нечего, так что придется выбрать одну из дверей')
    timer = 3
    while timer != 0:
        choice = input().lower()
        if choice == 'шпиль':
            print(
                'Дверь перед вами открывается, и вы видите лестницу, ведущую к колокольне кафедрального собора маленького бельгийского городка. '
                '\nВы решаете закосплеить фильм "Залечь на дно в Брюгге", и вам это удаётся. От полученных при приземлении травм вы умираете')
            break
        elif choice == 'ракушка':
            print(
                'Дверь перед вами открывается, и вы чувствуете на своей коже лёгкий морской бриз. Вы радостно выбегаете и попадаете на пляж. Дверь за вами закрывается и исчезает'
                'Нечего не остается, вы гуляете по пляжу и через некоторое время находите мяч с лицом из кровавого отиска ладони. Вы решаете назвать его Уилсон.'
                'Впереди вас ожидают нескончаемые годы одиночества, и лишь Уилсон будет пытаться их скрасить')
            break
        elif choice == 'костер':
            print(
                'Дверь перед вами открывается, и вы видите сверкающий красными искрами портал. Портал ведёт в ад, и медленно, но верно, утягивает туда и вас'
                '\nВы попали в ад. И тут не так уж и плохо. Играет рокешник, и какой-то мужик неожиданно даёт вам двустволку. До конца своих дней вы сражаетесь с ордами демонов, как герой')
            break
        elif choice == 'обернуться':
            print('Вы оборачиваетесь, и, неожиданно для себя, видите скрытую полумраком дверь'
                  '\nВы открываете дверь и видите там коридор, в конце которого горит огромная надпись ВЫХОД'
                  '\nВы бежите к ней и спасаетесь')
            break
        else:
            timer -= 1
            print('Стены сжимаются')
            if timer == 0:
                print('Стены комнаты сжались окончательно, и сделали из вашего тела лепёшку')


def mail():  # Задание 2.2
    print('Введите логин и резервный адрес электронной почты: ')
    login = input()
    email = input()
    if login.find('@') != -1:
        print('Некорректный логин')
    elif email.find('@') == -1:
        print('Некорректный адрес почты')
    else:
        print('ОК')


def short_talk():  # Задание 2.3
    print('Добрый день! Как ваше настроение сегодня?')
    good = ['хорошее', 'круто', 'балдеж', 'отлично']
    bad = ['ужасно', 'плохо', 'фигово', 'не балдеж']
    answer = input()
    if answer in good:
        print('Отлично, у меня тоже всё хорошо:)')
    elif answer in bad:
        print('Ничего, всё наладится')
    else:
        print('Извините, я вас не понимаю')


def yes_or_not():  # Задание 2.4
    first = input()
    second = input()
    if first == 'да' or first == 'нет':
        if second == 'да' or second == 'нет':
            print('ВЕРНО')
        else:
            print('НЕВЕРНО')
    else:
        print('НЕВЕРНО')


def plus_minus():  # Задание 3.1
    print('Введите одно число:')
    number = float(input())
    if number > 0:
        print('+')
    elif number < 0:
        print('-')
    else:
        print('0')


def calculator():  # Задание 3.2
    while 1:
        first = int(input())
        second = int(input())
        sign = input()
        if sign == '+':
            print(first + second)
        elif sign == '-':
            print(first - second)
        elif sign == '*':
            print(first * second)
        elif sign == '/' and second != 0:
            print(first / second)
        else:
            print('888888')


def bissextile():  # Задание 3.3
    print('Введите год:')
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('Високосный')
    else:
        print('Не високосный')


def even_odd():  # Задание 3.4
    while 1:
        number = int(input())
        if number % 2 == 0:
            print('Чётный')
        else:
            print('Нечётный')


def card():  # Задание 3.5
    print('Введите самое длинное имя, которое только сможете придумать')
    length = len(input()) * 2 + 3
    print(length)


def safety():  # Задание 3.6
    print('Введите трехзначный код для сейфа')
    code = int(input())
    if code % 10 == code // 10 % 10 == code // 100:
        print('В числе все цифры одинаковые')
    elif (code % 10 == code // 10 % 10) or (code // 10 % 10 == code // 100) or (code // 100 == code % 10):
        print('В числе две цифры одинаковые')
    else:
        print('ОК')


def nice_number():  # Задание 3.7
    number = int(input())
    if (int(number % 10 + number // 100) / 2) == number // 10 % 10:
        print('Ваше число красивое')
    else:
        print('Ваше число некрасивое')


def build_number():  # Задание 3.8
    number = int(input())
    first = number // 100 + number // 10 % 10
    second = number // 10 % 10 + number % 10
    if first > second:
        print(str(first) + str(second))
    else:
        print(str(second) + str(first))


def telegram():  # Задание 3.9
    message = len(input()) * 40
    print(str(message // 100) + 'р. ' + str(message % 100) + 'коп.')


def how_many_strings():  # Задание 4.1
    count = 0
    speech = []
    while speech != 'Спасибо.':
        speech = input()
        count += 1
    print(count)


def middle():  # Задание 4.2
    temperature = 0
    count = 0
    while temperature >= -300:
        need = float(input())
        temperature += need
        count += 1
    temperature -= need
    mid = float(temperature / (count - 1))
    print(mid)


def degree_of_two():  # Задание 4.3
    count = 1
    n = 2
    number = int(input())
    while n * 2 <= number:
        n *= 2
        count += 1
    if n == number:
        print(count)
    else:
        print('НЕТ')


def password_check():  # Задание 4.4
    first = input()
    while len(first) < 8:
        print('Слишком короткий пароль')
        first = input()
    while first.find('123') != -1:
        print('Слишком простой пароль')
        first = input()
    second = input()
    if first != second:
        print('Пароли различаются')
    else:
        print('ОК')


def sirakuz():  # Задание 4.5
    number = int(input())
    counter = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
            counter += 1
        else:
            number = number * 3 + 1
            counter += 1
    print(counter)


def rounder():  # Задание 4.6
    number = 10
    while number % 10 == 0:
        number = int(input())


def treasure_one():  # Задание 4.7
    x = int(input())
    y = int(input())
    i = j = l = k = 0
    m = 0
    t = True
    N = ["север", "восток", "юг", "запад"]
    n = "север"
    a = ''
    while a != "стоп":
        a = input()
        if a == "вперёд":
            b = int(input())
            if m == 0:
                j += b
                l += 1
            elif m == 1:
                i += b
                l += 1
            elif m == 2:
                j -= b
                l += 1
            elif m == 3:
                i -= b
                l += 1
        elif a == "налево":
            m -= 1
            if m < 0:
                m = 3
                l += 1
        elif a == "направо":
            m += 1
            if m > 3:
                m = 0
                l += 1
        elif a == "разворот":
            if m == 0:
                m = 2
                l += 1
            elif m == 2:
                m = 0
                l += 1
            elif m == 1:
                m == 3
                l += 1
            elif m == 3:
                m == 1
                l += 1
        if j == y and i == x and t:
            t = False
            n = N[m]
            k = l
    print('')
    print(k)
    print(n)


def binary_search():  # Задание 4.8
    start = 1
    end = 1000
    mid = end
    answer = []

    print('Загадайте число от 1 до 1000, программа будет пытаться его угадать'
          '\n> если число больше, < если число меньше, = если число было угадано')
    while answer != '=':
        print(mid)
        answer = input()
        if answer == '<':
            end = mid
            mid = int(start + (end - start) / 2)
        elif answer == '>':
            start = mid
            mid = int(start + (end - start) / 2)
    print('Ваше число: ' + str(mid))


def lucky_island():  # Задание 5.1
    print('Введите дату рождения аборигена в виде ДД ММ ГГГГ')
    day = int(input())
    month = int(input())
    if month == 1:
        month = 11
    elif month == 2:
        month = 12
    elif month == 3:
        month = 1
    elif month == 4:
        month = 2
    elif month == 5:
        month = 3
    elif month == 6:
        month = 4
    elif month == 7:
        month = 5
    elif month == 8:
        month = 6
    elif month == 9:
        month = 7
    elif month == 10:
        month = 8
    elif month == 11:
        month = 9
    elif month == 12:
        month = 10

    year = int(input())
    century = year // 100
    number = year % 100
    print(century)
    print(number)
    week = day + ((13 * month - 1) // 5) + number + (number // 4 + century // 4 - 2 * century + 777)
    print(week)
    if month == 12:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print((week - 2) % 7)
        else:
            print((week - 1) % 7)
    else:
        print(week % 7)


def circus():  # Задание 5.2
    print('Введите желаемое кол-во камней: ')
    number = int(input())
    bag = 1
    counter = 0
    while bag != number:
        if number % 2 != 0:
            number -= 1
            counter += 1
        elif number % 2 == 0:
            number /= 2
            counter += 1
    print('Количество итераций: ' + str(counter))


def nim_two_pass():  # Задание 5.3
    a = int(input())
    b = int(input())
    while (a != 0) or (b != 0):
        n = int(input())
        c = int(input())
        if n == 1:
            a -= c
        elif n == 2:
            b -= c
        print(a, ' ', b)


def nickname():  # Задание 5.4
    a = int(input())
    c = 0
    b = 0
    while a != 0:
        if a > 3:
            b = random.randint(1, 3)
        else:
            b = a
        if a - b == 0:
            print('Вы проиграли')
            break
        else:
            a -= b
            print(b, ' ', a)
        c = int(input())
        if a - c == 0:
            print('Вы победили')
            break
        else:
            a -= c
            print(c, ' ', a)


def nickname_mini():  # Задание 5.5
    a = int(input())
    c = 0
    b = 0
    while a != 0:
        if a > 3:
            b = random.randint(1, 3)
        else:
            if a == 3:
                b = 2
            elif a == 2:
                b = 1
            else:
                b = 1
        if a - b == 0:
            print('Вы победили')
            break
        else:
            a -= b
            print(b, ' ', a)
        c = int(input())
        if a - c == 0:
            print('Вы проиграли')
            break
        else:
            a -= c
            print(c, ' ', a)


def nim_three_pass():  # Задание 5.6
    a = int(input())
    b = int(input())
    c = int(input())
    while (a != 0) or (b != 0) or (c != 0):
        i = int(input())
        n = int(input())
        if i == 1 and not (a - n < 0) and not (n < 0):
            a -= n
            print(a, ' ', b, ' ', c)
        elif i == 2 and not (b - n < 0) and not (n < 0):
            b -= n
            print(a, ' ', b, ' ', c)
        elif i == 3 and not (c - n < 0) and not (n < 0):
            c -= n
            print(a, ' ', b, ' ', c)


def nim_two():  # Задание 5.7
    a = int(input())
    b = int(input())
    n = 0
    while a != 0 or b != 0:
        if (a and b) != 0:
            i = random.randint(1, 2)
            if i == 1:
                if a % 2 == 0:
                    a //= 2
                else:
                    a -= 1
            else:
                if b % 2 == 0:
                    b //= 2
                else:
                    b -= 1
        elif a == 0:
            b -= b
            print('Вы проиграли')
            break
        elif b == 0:
            a -= a
            print('Вы проиграли')
            break
        print(a, ' ', b)
        i = int(input())
        if i == 1:
            while not (0 < n <= a):
                n = int(input())
            a -= n
            if a == 0 and b == 0:
                print('Вы выиграли')
                break
        elif i == 2:
            while not (0 < n <= b):
                n = int(input())
            b -= n
            if a == 0 and b == 0:
                print('Вы выиграли')
                break


def nim_three():  # Задание 5.8
    a = int(input())
    b = int(input())
    c = int(input())
    n = 0
    while a != 0 or b != 0 or c != 0:
        if (a and b and c) != 0:
            i = random.randint(1, 3)
            if i == 1:
                if a % 2 == 0:
                    a //= 2
                else:
                    a -= 1
            elif i == 2:
                if b % 2 == 0:
                    b //= 2
                else:
                    b -= 1
            elif i == 3:
                if c % 2 == 0:
                    c //= 2
                else:
                    c -= 1
        elif a == 0 and c == 0:
            b -= b
            print('Вы проиграли')
            break
        elif b == 0 and c == 0:
            a -= a
            print('Вы проиграли')
            break
        elif b == 0 and a == 0:
            c -= c
            print('Вы проиграли')
            break
        print(a, ' ', b, ' ', c)
        i = int(input())
        if i == 1:
            while not (0 < n <= a):
                n = int(input())
            a -= n
            if a == 0 and b == 0 and c == 0:
                print('Вы выиграли')
                break
        elif i == 2:
            while not (0 < n <= b):
                n = int(input())
            b -= n
            if a == 0 and b == 0 and c == 0:
                print('Вы выиграли')
                break
        elif i == 3:
            while not (0 < n <= c):
                n = int(input())
            c -= n
            if a == 0 and b == 0 and c == 0:
                print('Вы выиграли')
                break


def backward_counter():  # Задание 6.1
    print('Введите количество секунд до запуска: ')
    sec = int(input())
    if sec < 0:
        print('Пуск!')
    else:
        while sec > 0:
            print('Осталось секунд:', sec)
            time.sleep(1)
            sec -= 1
        print('Пуск!')


def pyramid():  # Задание 6.2
    print('Введите высоту пирамиды: ')
    height = int(input())
    layer = 1
    base = 1
    while layer <= height:
        print(' ' * int(height - layer) + '*' * base)
        layer += 1
        base += 2


def divisibility_test():  # Задание 6.3
    counter = 0
    while counter <= 16:
        symbol = int(input())
        if symbol == 0:
            print('Введите другое число')
        elif counter % symbol == 0:
            print('ДА')
            counter += 1
        else:
            print('НЕТ')
            counter += 1


def smarter_than_average():  # Задание 6.4
    number = int(input())
    i = 1
    base = 0
    while i in range(number + 1):
        iq = int(input())
        base += iq
        if iq > base / i:
            print('>')
        elif iq < base / i:
            print('<')
        else:
            print('0')
        i += 1


def Terminator_v_Godzilla():  # Задание 6.5
    n = int(input())
    s = 0
    for i in range(0, n):
        a = int(input())
        b = int(input())
        s = s + a / b
    num = 0
    k = 1
    for i in range(int(input())):
        a, b = int(input()), int(input())
        num = num * b + a * k
        k *= b
    x, y = num, k
    while y > 0:
        x, y = y, x % y
    print(num // x, '/', k // x)


def riman_function():  # Задание 6.6
    n = int(input())
    a = 0
    p = 3.141592653589793
    for i in range(0, n):
        a = a + (1 / ((i + 1) ** 2))
    print((p ** 2) / a)


def row_sum():  # Задание 6.7
    counter = int(input())
    value = 0
    while counter > 0:
        if counter % 2 != 0:
            value += int(input())
        else:
            value -= int(input())
        counter -= 1
    print(value)


def find_cat_one():  # Задание 7.1
    counter = int(input())
    success = 0
    while counter > 0:
        string = input().lower().find('кот')
        if string != -1:
            success = 1
        counter -= 1
    if success == 1:
        print('МЯУ')
    else:
        print('НЕТ')


def find_cat_two():  # Задание 7.2
    counter = 1
    stop = 0
    string = []
    while string != 'СТОП':
        string = input()
        if string.lower().find('кот') != -1:
            if stop == 0:
                stop = counter
        counter += 1
    if stop == 0:
        print('-1')
    else:
        print(stop)


def find_cat_break_one():  # Задание 7.3
    counter = int(input())
    success = 0
    while counter > 0:
        string = input().lower().find('кот')
        if string != -1:
            print('МЯУ')
            success = 1
            break
        counter -= 1
    if success == 0:
        print('НЕТ')


def find_cat_break_two():  # Задание 7.4
    a = ''
    t = b = True
    i = 0
    while b:
        i += 1
        a = input()
        if "СТОП" in a:
            b = False
        if ("Кот" in a) or ("кот" in a):
            t = False
            print(i)
            break
    if t:
        print(-1)


def find_cat_three():  # Задание 7.5
    a = ''
    t = b = True
    c = i = d = 0
    while b:
        i += 1
        a = input()
        if "СТОП" in a:
            b = False
        if ("Кот" in a) or ("кот" in a):
            t = False
            d += 1
            if c == 0:
                c = i
    if t:
        print(d, ' ', -1)
    else:
        print(d, ' ', c)


def map_two():  # Задание 7.6
    x = int(input())
    y = int(input())
    i = j = l = k = 0
    m = 0
    t = True
    N = ["север", "восток", "юг", "запад"]
    n = "север"
    a = ''
    while a != "стоп":
        a = input()
        if a == "юг":
            b = int(input())
            j -= b
            l += 1
        elif a == "север":
            b = int(input())
            j += b
            l += 1
        elif a == "запад":
            b = int(input())
            i -= b
            l += 1
        elif a == "восток":
            b = int(input())
            i += b
            l += 1
        if j == y and i == x and t:
            t = False
            k = l
    print(k)


def find_cat_four():  # Задание 7.7
    n = int(input())
    a = ''
    t = True
    for i in range(0, n):
        a = input()
        if ("Кот" in a) or ("кот" in a):
            t = False
        if ("Пёс" in a) or ("пёс" in a):
            t = True
    if t:
        print("НЕТ")
    else:
        print("МЯУ")


def dance_school():  # Задание 7.8
    n = int(input())
    i = 0
    b = 1
    while n > 0:
        a = input()
        if a == "раз" and b == 1:
            i += 1
            b += 1
        elif a == "два" and b == 2:
            i += 1
            b += 1
        elif a == "три" and b == 3:
            i += 1
            b += 1
        elif a == "четыре" and b == 4:
            i += 1
            b = 1
        else:
            print("Правильных отсчётов было ", i, ", но теперь вы ошиблись.")
            i = 0
            b = 1
            n -= 1
            if not (n > 0):
                print("На сегодня хватит.")
                break


def many_use_calculator():  # Задание 7.9
    a = ''
    list = []
    b = i = c = 0
    n = 1
    t = False
    while a != 'x':
        a = input()
        if a == 'x':
            if t:
                list.append(str(b))
                i += 1
            for g in range(0, i):
                print(list[g])
            break
        else:
            if a != ("+" or "-" or "*" or "/" or "%" or "!" or "x") and not (t):
                b = int(a)
                t = True
            if a == '+' and t:
                c = int(input())
                list.append(str(b + c))
                t = False
                i += 1
            elif a == '-' and t:
                c = int(input())
                list.append(str(b - c))
                t = False
                i += 1
            elif a == '*' and t:
                c = int(input())
                list.append(str(b * c))
                t = False
                i += 1
            elif a == '/' and t:
                c = int(input())
                if c != 0:
                    list.append(
                        str(b // c))  # почему-то делает неправильный вывод при 100/9(если там уже есть какие-то числа), но в пустой лист записывает правильный ответ
                    t = False
                    i += 1
            elif a == '%' and t:
                c = int(input())
                if c != 0:
                    list.append(str(b / c))
                    t = False
                    i += 1
            elif a == '!' and b > 0:
                for m in range(1, b + 1):
                    n *= m
                list.append(str(n))
                t = False
                i += 1


def broker_bot():  # Задание 7.10
    n = -1
    a = int(input())
    bought = sell = 0
    t = j = True
    while n != 0:
        n = int(input())
        if n > a and t and j:
            bought = n
            t = False
        if n < a and not (t) and j:
            sell = n
            j = False
        a = n
    print(bought, sell, sell - bought)


def table():  # Задание 8.1
    ii = int(input())
    jj = int(input())
    for j in range(1, jj + 1):
        print(*(i / j for i in range(1, ii + 1)), sep=' ')


def draw_rectangle():  # Задание 8.2
    a = int(input())
    b = int(input())
    c = input()
    print(c * b)
    for n in range(a - 2):
        print(c + ' ' * (b - 2) + c)
    print(c * b)


def newbie_farmer():  # Задание 8.3
    a = int(input())
    b = int(input())
    for n in range(1, a // 20):
        for d in range(0, a // 10):
            for e in range(0, a // 5):
                if ((n * 20 + d * 10 + e * 5) == a) and (n + d + e == b):
                    print(n, ' ', d, ' ', e)
