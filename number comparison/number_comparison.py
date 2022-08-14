"""number comparison."""
# comparing three numbers and arranging them in ascending order,
# or finding a number between two others

rev = 'Y'
a = int(0)
b = int(0)
c = int(0)
# To ensure the cyclicity of the program,
# we will use the "WHILE" loop
# Для обеспечения цикличности программы
# будем использовать цикл "WHILE"
while rev == 'Y':
    # Первичная инициализация переменных внутри цикла
    # Primary initialization of variables inside the loop
    a = int(0)
    b = int(0)
    c = int(0)
    rev = 'N'
    print('\n##################################################\n')
    print('Введите значение первого числа')
    print('Enter the value of the first number')
    a = int(input('a = '))
    print('\nВведите значение второго числа')
    print('Enter the value of the second number')
    b = int(input('b = '))
    print('\nВведите значение третьего числа')
    print('Enter the value of the third number')
    c = int(input('с = '))
    # Проверка на ввод нуля во всех переменных
    # Checking for zero input in all variables
    if a == 0 and b == 0 and c == 0:
        rev = 'Y'
        print('Вы ввели значение всех чисел равное нулю.')
        print('Попробуйте ещё раз. :-)')
        print('You entered the value of all numbers equal to zero.')
        print('Try again. :-)')
        continue
    # Проверка на ввод одинаковых значений
    # Checking for the same values
    elif a == b and b == c:
        rev = 'Y'
        print('Вы ввели одинаковые значения всех чисел')
        print('Попробуйте ещё раз. :-)')
        print('You entered the same values for all numbers')
        print('Try again. :-)')
        continue
    elif a == b:
        rev = 'Y'
        print('Вы ввели одинаковые значения чисел "a" и "b"')
        print('Попробуйте ещё раз. :-)')
        print('You entered the same values for the numbers "a" and "b"')
        print('Try again. :-)')
        continue
    elif a == c:
        rev = 'Y'
        print('Вы ввели одинаковые значения чисел "a" и "c"')
        print('Попробуйте ещё раз. :-)')
        print('You entered the same values for the numbers "a" and "c"')
        print('Try again. :-)')
        continue
    elif b == c:
        rev = 'Y'
        print('Вы ввели одинаковые значения чисел "b" и "c"')
        print('Попробуйте ещё раз. :-)')
        print('You entered the same values for the numbers "b" and "c"')
        print('Try again. :-)')
        continue
    # Начинаем поиск числа лежащего между двумя другими
    # Start searching for a number lying between two others
    print('\nПроизведя сложнейшие изыскания, мы пришли к выводу')
    print('что представленные к рассмотрению числа расположились')
    print('в следующем порядке:')
    print('Having made the most difficult research, we came to the conclusion')
    print('that the numbers presented for consideration were arranged')
    print('in the following order:')
    if a > b:
        if c > a:
            print('"c" > "a" > "b"')
            print(str(c) + ' > ' + str(a) + ' > ' + str(b))
        elif b > c:
            print('"a" > "b" > "c"')
            print(str(a) + ' > ' + str(b) + ' > ' + str(c))
        elif c > b:
            print('"a" > "c" > "b"')
            print(str(a) + ' > ' + str(c) + ' > ' + str(b))
    elif b > a:
        if c > b:
            print('"c" > "b" > "a"')
            print(str(c) + ' > ' + str(b) + ' > ' + str(a))
        elif a > c:
            print('"b" > "a" > "c"')
            print(str(b) + ' > ' + str(a) + ' > ' + str(c))
        elif c > a:
            print('"c" > "b" > "a"')
            print(str(c) + ' > ' + str(b) + ' > ' + str(a))
    print('\n##################################################\n')
    print('Попробуем ещё раз?')
    print("Let's try again?")
    rev = input('Y/N ')
