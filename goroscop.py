import sys

number1 = 1
number2 = 2
number3 = 3
number4 = 4
number5 = 5
number6 = 6
number7 = 7
number8 = 8
number9 = 9
number10 = 10
number11 = 11
number12 = 12
while True:
    date_string = input('Введите число месяца: ')
    error = False;
    #  Validate type of date
    try:
        date_int = int(date_string)
    except ValueError:
        try:
            val = float(date_string)
            print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No.. input is not a number. It's a string")
        finally:
            error = True
    if error == False:
        if date_int == number1:
            print('Водолей')
        if date_int == number2:
            print('Рыбы')
        if date_int == number3:
            print('Овен')
        if date_int == number4:
            print('Телец')
        if date_int == number5:
            print('Близнецы')
        if date_int == number6:
            print('Рак')
        if date_int == number7:
            print('Лев')
        if date_int == number8:
            print('Дева')
        if date_int == number9:
            print('Весы')
        if date_int == number10:
            print('Скорпион')
        if date_int == number11:
            print('Стрелец')
        if date_int == number12:
            print('Козерог')

        replay = input("Want to continue? ").lower()
        print(replay)
        if replay in ("yes", "y"):
            continue
        elif replay in ("no", "n"):
            raise SystemExit
        else:
           print("Sorry, I didn't understand that.")

