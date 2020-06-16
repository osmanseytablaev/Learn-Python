import time
def my_first_decorator(func):
    def decorator():
        print('Декоратор используется до вызова')
    decorator()
@my_first_decorator
def hi():
    print('Hi')
try:
    print('Hi')
    time.sleep(2)
    print('Goodbye')
    time.sleep(2)
    print('Decorator!!!')
    time.sleep(2)
    print('Decorator!!!')
    time.sleep(2)
except KeyboardInterrupt:
    print('Stop')




