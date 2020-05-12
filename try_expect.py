try:
    f = open('test.docs', 'rb')
    s = f.read()
    f.close()
except IOError:
    print("Невозможно открыть файл")