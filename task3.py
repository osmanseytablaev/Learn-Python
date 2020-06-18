def car(turbo=100):
    points = 0
    if turbo < 70:
        print("OK")
    if turbo == 75:
        points += 2
        print("Points: 2")
    if turbo == 80:
        points += 4
        print("Points: 4")
    if turbo == 85:
        points += 6
        print("Points: 6")
    if turbo == 90:
        points += 8
        print("Points: 8")
    if turbo == 95:
        points += 10
        print("Points: 10")
    if turbo == 100:
        points += 12
        print("Points: 12")
    if points == 12:
        print("Лицензия приостановлена")
car()
    
    
    