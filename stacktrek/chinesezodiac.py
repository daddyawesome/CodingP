from numpy import intp

enter_Year = int(input("year:"))

modyear = enter_Year % 12

if modyear == 8:
    print("Dragon")
elif modyear == 9:
    print("Snake")
elif modyear == 10:
    print("Horse")
elif modyear == 11:
    print("Sheep")
elif modyear == 0:
    print("Monkey")
elif modyear == 1:
    print("Rooster")
elif modyear == 2:
    print("Dog")
elif modyear == 3:
    print("Boar")
elif modyear == 4:
    print("Rat")
elif modyear == 5:
    print("Ox")
elif modyear == 6:
    print("Tiger")
else: 
    print("Hare")