"""Решение квадратного уравнения."""


a = float(0.0)  # Значение компоненты А в квадратном уравнении."""
b = float(0.0)  # Значение компоненты B в квадратном уравнении."""
c = float(0.0)  # Значение компоненты C в квадратном уравнении."""
d = float(0.0)  # Вычисляемое значение Дискриминанта
x1 = float(0.0)  # Первое решение
x2 = float(0.0)  # Второе решение
rep = 'Y'

while rep == 'Y':
    print('Решение квадратичного уравнения')
    print('ax^2 + bx + c = 0')
    a = float(input('Введите значение компоненты "a":'))  # Вводим значение "а"
    b = float(input('Введите значение компоненты "b":'))  # Вводим значение "b"
    c = float(input('Введите значение компоненты "c":'))  # Вводим значение "c"
    if a != 0.0 and b != 0.0 and c != 0.0:  # Проверяем значение переменных
        d = b**2-4*a*c  # Вычисляем дискриминант
        if d > 0:  # Проверяем дискриминант
            print(' ')
            print('Дискриминант больше 0')
            print('уравнение имеет два решения')
            x1 = (-1*b-d**0.5)/(2*a)  # Первое решение
            x2 = (-1*b+d**0.5)/(2*a)  # Второе решение
            print('Первое решение х = ' + x1)
            print('Второе решение х = ' + x2)
        elif d < 0:  # Проверяем дискреминант
            print(' ')
            print('Дискриминант меньше нуля')
            print('уравнение не имеет решений')
        else:
            print(' ')
            print('Дискриминант равен нулю')
            print('уравнение имеет одно решение')
            x1 = (-1*b)/(2*a)
            x2 = 0.0
            print('x = ' + x1)
    elif a != 0 and b != 0 and c == 0:
        print(' ')
        print('Компонента c = 0')
        print('уравнение принимает вид')
        print('ax^2 + bx = 0')
        print(' ')
        print('Уравнение имеет два решения')
        print('x1 = 0')
        x1 == 0
        x2 == -1*(b/a)
        print('x2 = ' + x2)
    elif a != 0 and b == 0 and c != 0:
        print(' ')
        print('Компонента b = 0')
        print('уравнение принимает вид')
        print('ax^2 + c = 0')
        print('и имеет смысл только при отрицательных значениях компоненты с')
        print(' ')
        if c > 0:
            print('!!!')
            print('Уравнение не имеет смысла')
        else:
            x1 = (c/a)**0.5
            x2 = -1*x1
            print('Уравнение имеет два решения')
            print('Первое решение x1 = ' + x1)
            print('Второе решение x2 = ' + x2)
    elif a == 0 and b != 0 and c != 0:
        print(' ')
        print('Компонента a = 0')
        print('уравнение принимает вид')
        print('bx + c = 0')
        print(' ')
        x1 = (-1*c)/b
        print('Решение уравнения x1 = ' + x1)
        x2 = 0.0
    else:
        print('a = ' + a)
        print('b = ' + b)
        print('c = ' + c)
    print(' ')
    rep = 'N'
    print('Продолжим?')
    rep = input('Введите "Y" если да, или "N" если нет!')
