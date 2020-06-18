def fizz_buzz():
    number = 6
    if number / 3:
        print("Fizz")
    elif number / 5:
        print("Buzz")
    elif number / 3 and 5:
        print("FizzBuzz")
    else:
        print(number)
fizz_buzz()