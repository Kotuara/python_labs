def books_for_summer():  # Задание 9.1
    library = int(input())
    task = int(input())
    books = []
    i = 0
    while i < library:
        books.append(input())
        i += 1
    i = 0
    while i < task:
        taskbooks = input()
        if taskbooks in books:
            print('YES')
        else: print('NO')
        i += 1


def attendance():  # Задание 9.2
    lessons = int(input())
    attend = []
    all = []
    i = j = 0
    while i < lessons:
        pupils = int(input())
        while j < pupils:
            student = input()
            attend.append(student)
            j += 1
            if attend.count(student) == lessons:
                all.append(student)
        j = 0
        i += 1
    for x in all:
        print(x)


def namesakes():  # Задание 9.3
    amount = int(input())
    surnames = []
    i = 0
    sakes = 0
    while i < amount:
        man = input()
        surnames.append(man)
        i += 1
    sakes = {i: surnames.count(i) for i in surnames}
    print(sakes)


def recepies():  # Задание 9.4
    m = int(input())
    ingredients = []
    i = j = k = 0
    while i < m:
        ingredients.append(input())
        i += 1
    n = int(input())
    while j < n:
        recipe = input()
        m = int(input())
        while k < m:
            ingredient = input()
            if ingredient in ingredients == m:
                print(recipe)
            k += 1
        j += 1


def new_recepies():  # Задание 9.5
    m = int(input())
    dishes = []
    i = j = k = 0
    while i < m:
        dishes.append(input())
        i += 1
    n = int(input())
    while j < n:
        m = int(input())
        while k < m:
            used = input()
            if used in dishes:
                dishes.remove(used)
            k += 1
        j += 1
    for x in dishes:
        print(x)


def letter():  # Задание 10.1
    word = input()
    index = int(input())
    if 0 < index <= len(word):
        print(word[index-1].capitalize())
    else:
        print('ОШИБКА')


def caesar_knows():  # Задание 10.2
    step = int(input())
    message = input()
    s = set()
    for i in range(len(message)):
        if message[i] == ' ':
            print(end=' ')
        elif message[i] == ',':
            print(',', end='')
        elif message[i] == '!':
            print('!', end='')
        elif message[i] == '.':
            print('.', end='')
        elif message[i] == '?':
            print('?', end='')
        else:
            k = ord(message[i])
            l = k + step
            print(chr(l), end='')


def say_a():  # Задание 10.3
    message = input().lower()
    if message[0] == 'а':
        print('ДА')
    else:
        print('НЕТ')


def last_letter_two():  # Задание 10.4
    message = input()
    print(message[-1])


def keep_saying_a():  # Задание 10.5
    message = 'а'
    while message[0].lower() == 'а':
        message = input()


def snail():  # Задание 10.6
    trail = input()
    a = trail[1::].replace('V', '!V!').split('!')
    current_pos = 0
    k = 1 if len(trail) == 1 or trail[1] == 'V' else 0
    for i in a:
        if i == '':
            continue
        elif i[0] == '<':
            current_pos -= len(i)
            print(current_pos * ' ' + trail[0]  + i.replace('<', trail[0]))
            k = 0
        elif i[0] == '>':
            print(current_pos * ' ' + trail[0]  + i.replace('>', trail[0]))
            current_pos += len(i)
            k = 0
        elif i[0] == 'V':
            if k :
                print(current_pos * ' ' + trail[0])
            k = 1
    if k :
        print(current_pos * ' ' + trail[0])


def rosenkraz_and_gildenstein():  # Задание 11.1
    message = input()
    counter = 0
    max = 0
    for i in range (len(message)):
        if message[i] == 'о':
            counter += 1
        else:
            counter = 0
        if counter > max:
            max = counter
    print(max)


def filter():  # Задание 11.2
    n = int(input())
    i = 0
    list = []
    while i < n:
        s = input().replace('%%', '')
        if s.find('####') != -1:
            s = ''
        else:
            list.append(s)
        i += 1
    for x in list:
        print(x)


def exact_letter():  # Задание 11.3
    message = input()
    fav_digit = int(input())
    fav_letter = input()
    if fav_digit > len(message):
        print('ОШИБКА')
    elif len(fav_letter) > 1:
        print('ОШИБКА')
    else:
        if message[fav_digit - 1] == fav_letter:
            print('ДА')
        else:
            print('НЕТ')


def minificator():  # Задание 11.4
    n = int(input())
    list = []
    for i in range(n):
        string = input()
        for x in string:
            if string[x] == '#':
               string = (string[:x])
        print(string)
#Не понимаю как делать


def eat_letters():  # Задание 11.5
    message = input()
    i = 0
    for i in range(int(len(message))):
        print(message[i: -i])
        i += 1


def white_list():  # Задание 12.1
    n = int(input())
    white = []
    i = j = 0
    while i < n:
        white.append(input())
        i += 1
    n = int(input())
    while j < n:
        word = input()
        if word in white:
            print(word)
        j += 1


def check_check():  # Задание 12.2
    n = input()
    s = []
    s1 = []
    b = 0
    lot, itogo = int(n[:4]), int(n[4:])
    for i in range(lot):
        a = input()
        price, kolvo, summ = int(a[0:7]), int(a[8:12]), int(a[13:18])
        if price * kolvo != summ:
            s.append(i + 1)
        summ1 = kolvo * price
        s1.append(summ1)
    for i in s1:
        b += i
    print(itogo - b)
    for i in s:
        print(i, end=' ')


def buy_list():  # Задание 12.3
    n = int(input())
    i = 0
    list = [None]*n
    while n > i:
        list[n-1] = (input(), int(input()))
        n -= 1
    for x in list:
        print(x)


def RLE():  # Задание 12.4
    string = input()
    run_lenght = 1
    for i in range(len(string)-1):
        if i <= len(string):
            if string[i] == string[i + 1]:
                run_lenght += 1
            else:
                a = string[i]
                print(run_lenght, string[i])
                run_lenght = 1
    print(run_lenght, string[i])


def periodical_decimal():  #Задание 12.5
    n = int(input())
    r = 1
    rr = []
    dd = []
    while r not in rr:
        rr.append(r)
        dd.append(10*r//n)
        r = 10*r%n
    print(*dd[rr.index(r):], sep = "")


def big_letters():  #Задание 12.6
    alphabet = {'A': [' *   ', '* *  ', '***  ', '* *  ', '* *  '],
         'B': ['**   ', '* *  ', '**   ', '* *  ', '**   '],
         'C': [' *   ', '* *  ', '*    ', '* *  ', ' *   ']}
    string = input()
    for i in range(5):
        for x in string:
            print(alphabet.get(x)[i], end='')
        print()


def scaling():  #Задание 12.7
    height = int(input())
    width = int(input())
    list1 = []
    list2 = []
    for i in range(height):
        list1.append(input())
    for i in list1[::2]:
        list2.append(i[::2])
    for i in list2:
        print(i)


def thimbles():  #Задание 13.1
    string = [input() for i in range(int(input()))]
    for i in range(int(input())):
        tmp = [string[int(input())-1] for j in range(int(input()))]
        string = tmp
    print('\n'.join(string))


def reverse_sort():  #Задание 13.2
    n = int(input())
    list = []
    for i in range(n):
        list.append(int(input()))
    list.sort(reverse=True)
    for x in list:
        print(x)


def a_twentyseven():  #Задание 13.3
    res = []
    for _ in range(int(input())):
        res.append(sum((x == y for x, y in zip(res, reversed(res)))))
    print(*res, sep='\n')


def two_ways():  #Задание 13.4
    n = int(input())
    first = [int(input()) for i in range(n)]
    second = first[:]
    training = int(input())
    for i in range(training):
        brother = int(input())
        if brother == 1:
            first[int(input())] += int(input())
        elif brother == 2:
            second[int(input())] += int(input())
    print(*first)
    print(*second)
    equal = 0
    for i in range(len(first)):
        if first[i] == second[i]:
            equal += 1
    print(equal)


def final_not_final():  #Задание 13.5
    pass

def big_letters2():  #Задание 13.6
    alphabet = {'A': [' *   ', '* *  ', '***  ', '* *  ', '* *  '], 'B': ['**   ', '* *  ', '**   ', '* *  ', '**   '],
     'C': [' *   ', '* *  ', '*    ', '* *  ', ' *   '], 'D': ['**   ', '* *  ', '* *  ', '* *  ', '**   '],
     'E': ['***  ', '*    ', '**   ', '*    ', '***  '], 'F': ['***  ', '*    ', '**   ', '*    ', '*    '],
     'G': [' **  ', '*    ', '* *  ', '* *  ', ' **  '], 'H': ['* *  ', '* *  ', '***  ', '* *  ', '* *  '],
     'I': ['***  ', ' *   ', ' *   ', ' *   ', '***  '], 'J': [' **  ', '  *  ', '  *  ', '* *  ', ' *   '],
     'K': ['* *  ', '**   ', '*    ', '**   ', '* *  '], 'L': ['*    ', '*    ', '*    ', '*    ', '***  '],
     'M': ['* *  ', '***  ', '***  ', '***  ', '* *  '], 'N': ['* *  ', '***  ', '***  ', '* *  ', '* *  '],
     'O': ['***  ', '* *  ', '* *  ', '* *  ', '***  '], 'P': ['***  ', '* *  ', '***  ', '*    ', '*    '],
     'Q': ['***  ', '* *  ', '* *  ', '***  ', '***  '], 'R': ['**   ', '* *  ', '**   ', '* *  ', '* *  '],
     'S': [' **  ', '*    ', ' *   ', '  *  ', '**   '], 'T': ['***  ', ' *   ', ' *   ', ' *   ', ' *   '],
     'U': ['* *  ', '* *  ', '* *  ', '* *  ', '***  '], 'V': ['* *  ', '* *  ', '* *  ', '* *  ', ' *   '],
     'W': ['* *  ', '* *  ', '* *  ', '***  ', '* *  '], 'X': ['* *  ', '* *  ', ' *   ', '* *  ', '* *  '],
     'Y': ['* *  ', '* *  ', '* *  ', ' *   ', ' *   '], 'Z': ['***  ', '  *  ', ' *   ', '*    ', '***  ']}
    string = input()
    for i in range(5):
        for x in string:
            print(alphabet.get(x)[i], end='')
        print()


def total_decimation():  #Задание 13.7
    n = int(input())
    legion = []
    for i in range(n):
        legion.append(input())
    k = int(input())
    i = 0
    while i < n:
        print(legion[i])
        legion.pop(i)
        if i + k >= n:
            i = 0
        else:
            i += k-1
        n -= 1


def without_onion():  #Задание 14.1
    n = int(input())
    recepie = []
    for i in range(n):
        string = input()
        if string.find('лук') != -1:
            string = ''
        else:
            recepie.append(string)
    for x in recepie:
        print(x, end=' ')


def etc():  #Задание 14.2
    pass

def lighthousov():  #Задание 14.3
    string = input().split()
    for x in string:
        print(x)


def vertical_diagram():  #Задание 14.4
    n = list(map(int, input().split()))
    xmax = len(n)
    ymax = max(n)
    print('*'*(xmax+2))
    print('*'+' '*xmax+'*')
    for y in range(1, ymax+1):
        print(end='*')
        for nk in n:
            if nk >= ymax-y+1: print(end='*')
            else: print(end=' ')
        print('*')


def get():  #Задание 14.5
    a =[list(i.split("=")) for j in list(input().split("?")) for i in list(j.split("&"))][1:]
    b = input()
    for i in range(len(a)):
        if a[i][0] == b:
            print(a[i][1])


def Gatsby():  #Задание 15.1
    a = input()
    print(*[i for i in input().split() if a.upper() in i or a in i],sep='\n')


def symbol_without_space():  #Задание 15.2
     print(len(input().replace(' ', '')))


def longneck_eater():  #Задание 15.3
    s = input().lower()
    counter = 0
    for i in range(len(s)):
        if s.count(s[i]) > counter:
            counter = s.count(s[i])
    print(counter)


def stat_paradox():  #Задание 15.4
    pass


def queue():  #Задание 15.5
    n = int(input())
    q = []
    for _ in range(n):
        s = input().split()
        if 'встал' in s[1]:
            q.append(s[0])
        elif s[0] == 'Привет,':
            q.insert(q.index(s[1][:-1])+1, s[2])
        elif s[1] == 'хватит':
            q.remove(s[0][:-1])
    print(*q, sep='\n')


def bf():  #Задание 16.1
    s=[0 for i in range(30001)]
    pos = 0
    a = input()
    print(a)
    i=0
    while(i<len(a)):
        if a[i] == ">":
            pos = pos + 1
        elif a[i] == "<":
            pos = pos - 1
        elif a[i] == ".":
            print(s[pos])
        elif a[i] == "+":
            s[pos] = s[pos] + 1
            if s[pos]>255:
                s[pos]=0
        elif a[i] == "-":
            s[pos] = s[pos] - 1
            if s[pos]<0:
                s[pos]=255
        elif a[i] == '[':
            if s[pos] == 0:
                j=i+1
                c=1
                while(True):
                    if a[j]=='[':
                        c+=1
                    if a[j]==']':
                        c-=1
                    if c==0:
                        i=j
                        break
                    j+=1
        elif a[i] == ']':
            c=-1
            j=i-1
            while(True):
                if a[j]==']':
                    c-=1
                if a[j]=='[':
                    c+=1
                if c==0:
                    i=j-1
                    break
                j-=1

        i+=1


def csv():  #Задание 16.2
    string_list = [input().split(",") for i in range(int(input()))]
    for i in range(int(input())):
        string_number, word_number = [int(i) for i in input().split(",")]
        print(string_list[string_number][word_number])


def fight_the_bacteria():  #Задание 16.3
    n = int(input())
    field = []
    for i in range(n):
        field.append([0] * n)
    for a in range(n):
        for b in range(n):
            field[a][b] = int(input())
    k = int(input())
    for j in range(k):
        y = int(input())
        x = int(input())
        field[x][y] -= 8
        if x - 1 >= 0 and y - 1 >= 0:
            field[x - 1][y - 1] -= 4
        if x - 1 >= 0:
            field[x - 1][y] -= 4
        if y - 1 >= 0:
            field[x][y - 1] -= 4
        if x + 1 < n and y + 1 < n:
            field[x + 1][y + 1] -= 4
        if x + 1 < n:
            field[x + 1][y] -= 4
        if y + 1 < n:
            field[x][y + 1] -= 4
        if x - 1 >= 0 and y + 1 < n:
            field[x - 1][y + 1] -= 4
        if x + 1 < n and y - 1 >= 0:
            field[x + 1][y - 1] -= 4
    for c in range(n):
        for d in range(n):
            if field[c][d] < 0:
                field[c][d] = 0
    for i in range(n):
        field[i] = ' '.join(str(v) for v in field[i])
    print('\n'.join(field))


def economics():  #Задание 16.4
    n = int(input())
    s = [[]]

    for i in range(n - 1):
        s.append([int(j) for j in input().split()])

    station = input().split()
    a, a1 = int(station[0]), int(station[1])

    l = s[max(a, a1)][min(a, a1)]
    b = -1

    for i in range(n):
        if i != a and i != a1:
            if (l > s[max(a, i)][min(a, i)] + s[max(i, a1)][min(i, a1)]):
                l = s[max(i, a1)][min(i, a1)] + s[max(i, a1)][min(i, a1)]
                b = i

    if b != -1:
        print(b)
    else:
        print(a)


def transliteration():  #Задание 17.1
    alphabet = {'А': ['A'], 'Б': ['B'], 'В': ['V'], 'Г': ['G'],
    'Д': ['D'], 'Е': ['E'], 'Ё': ['E'], 'Ж': ['Zh'],
    'З': ['Z'], 'И': ['I'], 'Й': 'I', 'К': ['K'],
    'Л': ['L'], 'М': ['M'], 'Н': ['N'], 'О': ['O'],
    'П': ['P'], 'Р': ['R'], 'С': ['S'], 'Т': ['T'],
    'У': ['U'], 'Ф': ['F'], 'Х': ['Kh'], 'Ц': ['Tc'],
    'Ч': ['Ch'], 'Ш': ['Sh'], 'Щ': ['Shch'], 'Ы': ['Y'],
    'Э': ['E'], 'Ю': ['Iu'], 'Я': ['Ia'],
    'а': ['a'], 'б': ['b'], 'в': ['v'], 'г': ['g'],
    'д': ['d'], 'е': ['e'], 'ё': ['e'], 'ж': ['zh'],
    'з': ['z'],'и': ['i'], 'й': ['i'], 'к': ['k'],
    'л': ['l'], 'м': ['m'],'н': ['n'], 'о': ['o'],
    'п': ['p'], 'р': ['r'], 'с': ['s'], 'т': ['t'],
    'у': ['u'], 'ф': ['f'], 'х': ['kh'], 'ц': ['tc'],
    'ч': ['ch'], 'ш': ['sh'], 'щ': ['shch'], 'ы': ['y'],
    'э': ['e'], 'ъ': [''], 'ь': [''], 'ю': ['iu'],
    'я': ['ia'], ' ': [' '], ':': [':'], ',': [','], '.': ['.']}
    string = input()
    for x in string:
        print(*alphabet[x], end='')


def telephone():  #Задание 17.2
    book = {}
    n = int(input())
    for i in range(n):
        value, key = input().split()
        if key in book:
            book [key].append(value)
        else:
            book [key] = [value]
    m = int(input())
    for i in range(m):
        key = input()
        if key in book:
            print(*book [key])
        else:
            print('Нет в телефонной книге')


def birthdays():  #Задание 17.3
    birthday = {}
    n = int(input())
    for i in range(n):
        name, date, month = input().split()
        if month in birthday:
            birthday[month].append(name)
            birthday[month].append(date)
        else:
            birthday[month] = [name, date]
    m = int(input())
    for i in range(m):
        month = input()
        if month in birthday:
            print(*birthday[month])
        else:
            print()


def reposts():  #Задание 17.4
    n = int(input())
    post = input().split(' опубликовал пост, количество просмотров: ')
    popularity = {post[0]: [int(post[-1]), 'origin']}
    for _ in range(n - 1):
        post = input()
        reposter, post = post.split(' отрепостил пост у ')
        author, views = post.split(', количество просмотров: ')
        popularity[reposter] = [int(views), author]
        while author != 'origin':
            popularity[author][0] += int(views)
            author = popularity[author][1]
    for val in popularity.values():
        print(val[0])


def permissions():  #Задание 17.5
    ways = [input() for i in range(int(input()))]
    files = [input() for i in range(int(input()))]
    lst_ways = [x.split('/')[1:] for x in ways]
    lst_files = [x.split('/')[1:] for x in files]
    def check_permissions(ways, file):
        for x in ways:
            if len(file) < len(x):
                continue
            else:
                if x == file[:len(x)]:
                    return 'YES'
        return 'NO'
    for i in lst_files:
        print(check_permissions(lst_ways, i))



