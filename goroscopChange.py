import sys

начало январь = [01.01, 02.01, 03.01, 04.01, 05.01, 06.01, 07.01, 08.01, 09.01, 10.01, 11.01, 12.01, 13.01, 14.01, 15.01, 16.01, 17.01, 18.01, 19.01]
конец январь = [20.01, 21.01, 22.01, 23.01, 24.01, 25.01, 26.01, 27.01, 28.01, 29.01, 30.01, 31.01]
начало февраль = []
конец февраль = []
начало март = []
конец март = []
начало апрель = []
конец апрель = []
начало май = []
конец май = []
начало июнь = []
конец июнь = []
начало июль = []
конец июль = []
начало август = []
конец август = []
начало сентябрь = []
конец сентябрь = []
начало октябрь = []
конец октябрь = []
начало ноябрь = []
конец ноябрь = []
начало декабрь = [] 
конец декабрь = [22.12, 23.12, 24.12, 25.12, 26.12, 27.12, 28.12, 29.12, 30.12, 31.12]
while True:
    date_string = input('Введите число месяца: ')
    error = False;
    #  Validate type of date
    try:
        date_float = float(date_string)
    except ValueError:
        try:
            val = int(date_string)
            print("Input is a number. Number = ", val)
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
        if date_int == начало январь:
            print('Козерог')
        if date_int == конец декабрь:
            print('Козерог')
        replay = input("Want to continue? ").lower()
        print(replay)
        if replay in ("yes", "y"):
            continue
        elif replay in ("no", "n"):
            raise SystemExit
        else:
           print("Sorry, I didn't understand that.")